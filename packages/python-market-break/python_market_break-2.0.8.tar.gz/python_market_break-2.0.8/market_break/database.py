# database.py

import datetime as dt
from typing import Iterable

import pandas as pd
from sqlalchemy.orm.session import sessionmaker, Session
import sqlalchemy as db

from dataplace import ModelIO, Callback

from market_break.record import RecordRow, RecordTable, record_callback
from market_break.labels import (
    TIMESTAMP, DATETIME, RECEIVED_DATETIME, EXCHANGE, SYMBOL
)

__all__ = [
    "record_database_callback",
    "create_record_database_table",
    "tables_names",
    "table_columns",
    "extract_record_table",
    "extract_dataframe",
    "insert_database_records",
    "datetime_dataframe",
    "table_name",
    "Columns",
    "DIVIDER"
]

DIVIDER = "_"

def create_record_database_table(
        name: str, metadata: db.MetaData = None, columns: Iterable[str] = None
) -> db.Table:
    """
    Creates a table for records in a database.

    :param name: The name of the table to create.
    :param metadata: The metadata object of the database.
    :param columns: The column names for the table.

    :return: The created table object.
    """

    if columns is None:
        columns = RecordRow.KEYS

    return db.Table(
        name,
        metadata or db.MetaData(),
        *Columns.generate(columns, non_nullables=[TIMESTAMP], limit=64)
    )

def record_database_callback(
        engine: db.Engine,
        metadata: db.MetaData = None,
        table: db.Table = None
) -> Callback:
    """
    Creates a callback to store price data record row objects.

    :param engine: The database engine.
    :param metadata: The metadata of the database.
    :param table: The table object to store records in.

    :return: The callback object.
    """

    session_maker = sessionmaker(bind=engine)

    metadata = metadata or db.MetaData()

    async def wrapper(data: ModelIO) -> None:

        if not isinstance(data, tuple(callback.types)):
            return

        data: RecordRow

        insert_database_records(
            records=[dict(**data)],
            engine=engine,
            session_maker=session_maker,
            metadata=metadata,
            table=table or DIVIDER.join(data.signature)
        )

    callback = record_callback(wrapper)

    return callback

class Columns:

    @staticmethod
    def string_column(name: str, limit: int = 64) -> db.Column[str]:

        return db.Column(name, db.String(limit))

    @staticmethod
    def int_column(name: str, nullable: bool = True) -> db.Column[int]:

        return db.Column(name, db.Integer(), nullable=nullable)

    @staticmethod
    def float_column(name: str, nullable: bool = True) -> db.Column[float]:

        return db.Column(name, db.Float(), nullable=nullable)

    @staticmethod
    def datetime_column(name: str, nullable: bool = True) -> db.Column[dt.datetime]:

        return db.Column(name, db.DateTime(), nullable=nullable)

    COLUMNS_TYPES = {
        RecordRow.EXCHANGE: str,
        RecordRow.SYMBOL: str,
        RecordRow.TIMESTAMP: float,
        RecordRow.DATETIME: dt.datetime,
        RecordRow.RECEIVED_DATETIME: dt.datetime,
        RecordRow.OPEN: float,
        RecordRow.HIGH: float,
        RecordRow.LOW: float,
        RecordRow.CLOSE: float,
        RecordRow.BID: float,
        RecordRow.ASK: float,
        RecordRow.BID_VOLUME: float,
        RecordRow.ASK_VOLUME: float,
        RecordRow.SIDE: str
    }

    TYPES_GENERATORS = {
        str: string_column,
        int: int_column,
        float: float_column,
        dt.datetime: datetime_column
    }

    LIMIT = 'limit'
    NULLABLE = 'nullable'

    @staticmethod
    def generate(
            columns: Iterable[str],
            nullables: Iterable[str] | dict[str, bool] = None,
            non_nullables: Iterable[str] | dict[str, bool] = None,
            limited: Iterable[str] | dict[str, int] = None,
            limit: int = None,
            nullable: bool = None
    ) -> list[db.Column]:

        if nullables is None:
            nullables = ()

        if non_nullables is None:
            non_nullables = ()

        if limited is None:
            limited = ()

        if nullables is not None and not isinstance(nullables, dict):
            nullables = set(nullables)

        if non_nullables is not None and not isinstance(non_nullables, dict):
            non_nullables = set(non_nullables)

        generated = []

        for name in columns:
            kwargs = dict()

            column_type = Columns.COLUMNS_TYPES[name]

            if column_type in (int, float, dt.datetime):
                if name in nullables:
                    kwargs[Columns.NULLABLE] = (
                        nullables[name] if isinstance(nullables, dict) else True
                    )

                elif name in non_nullables:
                    kwargs[Columns.NULLABLE] = (
                        non_nullables[name] if isinstance(non_nullables, dict) else False
                    )

                elif nullable is not None:
                    kwargs[Columns.NULLABLE] = nullable

            if column_type is str:
                if name in limited:
                    kwargs[Columns.LIMIT] = (
                        limited[name] if isinstance(limited, dict) else limit
                    )

                elif limit is not None:
                    kwargs[Columns.LIMIT] = limit

            generated.append(
                Columns.TYPES_GENERATORS[column_type](name, **kwargs)
            )

        return generated

def insert_database_records(
        records: Iterable[dict[str, str | float | int | dt.datetime]],
        engine: db.Engine,
        metadata: db.MetaData = None,
        session: Session = None,
        session_maker: sessionmaker = None,
        table: str | db.Table = None,
) -> None:

    first = None

    for first in records:
        break

    if first is None:
        return

    metadata = metadata or db.MetaData()

    if table is None:
        if (EXCHANGE not in first) or (SYMBOL not in first):
            raise ValueError(
                "both 'exchange' and 'symbol' must be defined for "
                "records when table is not given."
            )

        table: str | db.Table = table_name(exchange=first[EXCHANGE], symbol=first[SYMBOL])

    if isinstance(table, str):
        if table not in metadata.tables:
            db.Table(
                table,
                metadata or db.MetaData(),
                *Columns.generate(first, non_nullables=[TIMESTAMP], limit=64)
            )

            metadata.create_all(engine)

        table: db.Table = metadata.tables[table]

    created = False

    if session is None:
        session_maker = session_maker or sessionmaker(bind=engine)

        session = session_maker()

        created = True

    for data in records:
        data = {key.lower(): value for key, value in data.items()}

        session.execute(db.insert(table).values(**data))

    session.commit()

    if created:
        session.close()

def table_name(exchange: str, symbol: str) -> str:

    return f"{exchange}_{symbol}"

def tables_names(engine: db.Engine) -> list[str]:

    return db.inspect(engine).get_table_names()

def table_columns(engine: db.Engine, table: str) -> list[dict[str, ...]]:

    return db.inspect(engine).get_columns(table)


def datetime_dataframe(data: pd.DataFrame, datetime: list[str] = None) -> pd.DataFrame:

    auto = False

    if datetime is None:
        datetime = [DATETIME, RECEIVED_DATETIME]

        auto = True

    for column in (datetime or ()):
        if (column not in data) and auto:
            continue

        data[column] = pd.to_datetime(data[column], format='ISO8601')

    return data

def extract_dataframe(engine: db.Engine, table: str, datetime: list[str] = None) -> pd.DataFrame:

    # noinspection SqlDialectInspection
    data = pd.read_sql(f'SELECT * FROM "{table}"', engine)

    return datetime_dataframe(data, datetime=datetime)

def extract_record_table(engine: db.Engine, table: str) -> RecordTable:

    exchange, symbol = table.split(DIVIDER)

    return RecordTable(
        symbol=symbol,
        exchange=exchange,
        data=extract_dataframe(engine, table=table)
    )
# record.py

import datetime as dt
import numpy as np
from typing import (
    ClassVar, Generator, Mapping, Self, Awaitable, Callable, overload
)
from dataclasses import dataclass, field

import pandas as pd

from dataplace import ModelIO, SpaceStore, Callback

from market_break.labels import (
    BID, ASK, BID_VOLUME, ASK_VOLUME, OPEN, HIGH, LOW, CLOSE,
    TIMESTAMP, DATETIME, RECEIVED_DATETIME, EXCHANGE, SYMBOL,
    BUY, SELL, SIDE
)

__all__ = [
    "RecordTable",
    "RecordRow",
    "RecordStore",
    "record_store_callback",
    "record_callback"
]

type Value = dt.datetime | str | float | int
type JsonValue = str | float | int | str

@dataclass(slots=True, frozen=True)
class RecordRow(ModelIO, Mapping):
    """Represents a row in the record of the price data of a symbol."""

    exchange: str
    symbol: str
    timestamp: float
    datetime: dt.datetime
    received_datetime: dt.datetime
    open: float
    high: float
    low: float
    close: float
    bid: float
    ask: float
    bid_volume: float
    ask_volume: float
    side: str

    BID: ClassVar[str] = BID
    ASK: ClassVar[str] = ASK
    BID_VOLUME: ClassVar[str] = BID_VOLUME
    ASK_VOLUME: ClassVar[str] = ASK_VOLUME

    OPEN: ClassVar[str] = OPEN
    HIGH: ClassVar[str] = HIGH
    LOW: ClassVar[str] = LOW
    CLOSE: ClassVar[str] = CLOSE

    TIMESTAMP: ClassVar[str] = TIMESTAMP
    DATETIME: ClassVar[str] = DATETIME
    RECEIVED_DATETIME: ClassVar[str] = RECEIVED_DATETIME

    SIDE: ClassVar[str] = SIDE
    BUY: ClassVar[str] = BUY
    SELL: ClassVar[str] = SELL

    EXCHANGE: ClassVar[str] = EXCHANGE
    SYMBOL: ClassVar[str] = SYMBOL

    KEYS: ClassVar[tuple[str]] = (
        EXCHANGE, SYMBOL, TIMESTAMP, DATETIME, RECEIVED_DATETIME,
        OPEN, HIGH, LOW, CLOSE, BID, ASK, BID_VOLUME, ASK_VOLUME, SIDE
    )

    def __len__(self):

        return len(RecordRow.KEYS)

    def __iter__(self) -> Generator[str, None, None]:

        yield from RecordRow.KEYS

    def __getitem__(self, item: str) -> Value:

        return getattr(self, item)

    @property
    def signature(self) -> tuple[str, str]:

        return self.exchange, self.symbol

    def dump(self) -> dict[str, JsonValue]:

        data: dict[str, ...] = {**self}

        data[self.DATETIME] = data[self.DATETIME].isoformat()
        data[self.RECEIVED_DATETIME] = data[self.RECEIVED_DATETIME].isoformat()

        return data

    @classmethod
    def load(cls, data: dict[str, JsonValue]) -> Self:

        return cls(
            exchange=data[cls.EXCHANGE],
            symbol=data[cls.SYMBOL],
            timestamp=(
                data[cls.TIMESTAMP] if cls.TIMESTAMP in data else
                dt.datetime.now().timestamp()
            ),
            datetime=(
                dt.datetime.fromisoformat(data[cls.DATETIME])
                if cls.DATETIME in data else dt.datetime.now()
            ),
            received_datetime=(
                dt.datetime.fromisoformat(data[cls.RECEIVED_DATETIME])
                if cls.RECEIVED_DATETIME in data else dt.datetime.now()
            ),
            open=data.get(cls.OPEN, np.nan),
            high=data.get(cls.HIGH, np.nan),
            low=data.get(cls.LOW, np.nan),
            close=data.get(cls.CLOSE, np.nan),
            bid=data.get(cls.BID, np.nan),
            ask=data.get(cls.ASK, np.nan),
            bid_volume=data.get(cls.BID_VOLUME, np.nan),
            ask_volume=data.get(cls.ASK_VOLUME, np.nan),
            side=data.get(cls.SIDE, np.nan)
        )

    @classmethod
    def from_dict(cls, data: dict[str, JsonValue]) -> Self:

        return cls(**data)

    @classmethod
    def from_tuple(cls, data: tuple[JsonValue, ...]) -> Self:

        return cls.from_dict(dict(zip(cls.KEYS, data)))

@dataclass(slots=True)
class RecordTable(ModelIO):
    """Represents a table of price data record rows of a symbol."""

    symbol: str
    exchange: str
    memory: int = None
    data: pd.DataFrame = field(default=None, repr=False, hash=False)

    COLUMNS: ClassVar[tuple[str]] = RecordRow.KEYS

    EXCHANGE: ClassVar[str] = EXCHANGE
    SYMBOL: ClassVar[str] = SYMBOL

    MEMORY: ClassVar[str] = "memory"
    DATA: ClassVar[str] = "data"

    def __post_init__(self) -> None:

        if self.data is None:
            self.data = pd.DataFrame(
                {column: [] for column in self.COLUMNS},
                index=[]
            )

        else:
            self.validate_matching_columns()

    @overload
    def __getitem__(self, item: slice) -> Self:

        pass

    @overload
    def __getitem__(self, item: int) -> RecordRow:

        pass

    def __getitem__(self, item: slice | int) -> Self | RecordRow:

        if isinstance(item, slice):
            return RecordTable(
                symbol=self.symbol,
                exchange=self.exchange,
                memory=self.memory,
                data=self.data.iloc[item]
            )

        elif isinstance(item, int):
            return self.index_row(item)

    def __len__(self) -> int:

        return self.length

    def __hash__(self) -> int:

        return self.hash

    def __eq__(self, other: ...) -> bool:

        if type(other) is not type(self):
            return False

        other: RecordTable

        # noinspection PyTypeChecker
        return (
            (self.signature == other.signature) and
            (len(self.data.columns) == len(other.data.columns)) and
            (set(self.data.columns) == set(other.data.columns)) and
            len(self.data) == len(other.data) and
            all(self.data == other.data)
        )

    def __add__(self, other: ...) -> Self:

        if not isinstance(other, RecordTable):
            raise TypeError(
                f"both objects must be {RecordTable} "
                f"instances for addition, received: {type(other)}"
            )

        if self.signature != other.signature:
            raise ValueError(
                f"Cannot add two record objects of different signatures "
                f"({self.signature} and {other.signature})"
            )

        new = self.deepcopy()

        new.data = pd.concat([new.data, other.data])

        return new

    @property
    def length(self) -> int:

        return len(self.data)

    @property
    def is_empty(self) -> bool:

        return len(self.data) == 0

    @property
    def is_matching_columns(self) -> bool:

        return set(self.data.columns) != set(self.COLUMNS)

    @property
    def signature(self) -> tuple[str, str]:

        return self.exchange, self.symbol

    @property
    def hash(self) -> int:

        return hash(self.signature)

    def validate_not_empty(self) -> None:

        if self.is_empty:
            raise ValueError(f"No data in {repr(self)}")

    def validate_matching_columns(self) -> None:

        if self.is_matching_columns:
            raise ValueError(
                f"data columns and record column don't match "
                f"({self.data.columns} and {self.COLUMNS})"
            )

    @staticmethod
    def _process_data(data: dict[str, ...]) -> dict[str, ...]:

        if isinstance(data[DATETIME], pd.Timestamp):
            data[DATETIME] = data[DATETIME].to_pydatetime()

        if isinstance(data[RECEIVED_DATETIME], pd.Timestamp):
            data[RECEIVED_DATETIME] = data[RECEIVED_DATETIME].to_pydatetime()

        return data

    @staticmethod
    def _process_value(value: ...) -> ...:

        if isinstance(value, pd.Timestamp):
            value = value.to_pydatetime()

        return value

    def index_value(self, key: str, index: int) -> Value:

        self.validate_not_empty()

        return self._process_value(self.data[key].iloc[index])

    def last_value(self, key: str) -> Value:

        return self.index_value(key=key, index=-1)

    def first_value(self, key: str) -> Value:

        return self.index_value(key=key, index=0)

    def index_row(self, index: int) -> dict[str, Value]:

        self.validate_not_empty()

        return self._process_data(self.data.iloc[index].to_dict())

    def last_row(self) -> dict[str, Value]:

        return self.index_row(-1)

    def first_row(self) -> dict[str, Value]:

        return self.index_row(0)

    def first(self) -> RecordRow:

        self.validate_not_empty()

        return RecordRow(
            **self.first_row(),
            exchange=self.exchange, symbol=self.symbol
        )

    def last(self) -> RecordRow:

        self.validate_not_empty()

        return RecordRow(**self.last_row())

    def generate_rows(self) -> Generator[tuple[int, RecordRow], None, None]:

        for i, row in self.data.iterrows():
            yield i, RecordRow(**self._process_data(row.to_dict()))

    def rows(self) -> list[RecordRow]:

        return [data for i, data in self.generate_rows()]

    def append(self, data: RecordRow | dict[str, Value]) -> None:

        self.data.loc[len(self.data)] = {
            column: data[column] for column in self.COLUMNS
        }

        if self.memory:
            self.data.drop(
                self.data.index[:len(self.data) - self.memory],
                inplace=True
            )

    def pop(self, index: int) -> RecordRow:

        data = self.index_row(index=index)

        self.data.drop(index, inplace=True)

        return RecordRow(**data)

    def clear(self) -> None:

        self.data.drop(self.data.index, inplace=True)

    @classmethod
    def load(cls, data: dict[str, str | int | dict[str, JsonValue]]) -> Self:

        return cls(
            exchange=data[cls.EXCHANGE],
            symbol=data[cls.SYMBOL],
            memory=data.get(cls.MEMORY, None),
            data=pd.DataFrame.from_dict(data[cls.DATA], orient='columns')
        )

    def dump(self) -> dict[str, str | int | list[dict[str, JsonValue]]]:

        return {
            self.EXCHANGE: self.exchange,
            self.SYMBOL: self.symbol,
            self.MEMORY: self.memory,
            self.DATA: self.data.to_dict(orient='records')
        }

class RecordStore(SpaceStore[tuple[str, str], RecordTable]):
    """Represents a store for record tables."""

    def __init__(self) -> None:

        super().__init__(lambda data: data.signature, RecordTable)

    def map(self) -> dict[str, dict[str, list[RecordTable]]]:

        data = {}

        for (exchange, symbol), values in self.store.copy().items():
            if None in (exchange, symbol):
                continue

            data.setdefault(exchange, {})[symbol] = values

        return data

    def structure(self) -> dict[str, list[str]]:

        data = {}

        for (exchange, symbol), values in self.store.copy().items():
            if None in (exchange, symbol):
                continue

            data.setdefault(exchange, []).append(symbol)

        return data

    def exchanges(self) -> Generator[str, ..., ...]:

        for (exchange, symbol) in self.store:
            if None in (exchange, symbol):
                continue

            yield exchange

    def symbols(self) -> Generator[str, ..., ...]:

        for (exchange, symbol) in self.store:
            if None in (exchange, symbol):
                continue

            yield symbol

def record_callback(
        callback: Callable[[RecordRow], ... | Awaitable],
        preparation: Callable[[], Awaitable | ...] = None,
        enabled: bool = True,
        prepared: bool = False
) -> Callback:
    """
    Creates a callback to be called for price data record row objects.

    :param callback: The callback function to be called.
    :param preparation: The preparation function to be called.
    :param enabled: The value to enable the callback,
    :param prepared: The value to mark the callback as already prepared.

    :return: The callback object.
    """

    return Callback(
        callback=callback,
        types={RecordRow},
        preparation=preparation,
        enabled=enabled,
        prepared=prepared
    )

def record_store_callback(
        store: RecordStore,
        create: bool = True,
        add: bool = True,
        kwargs: dict[str, ...] = None
) -> Callback:
    """
    Creates a callback to store price data record row objects.

    :param store: The store object to store the record row in a table inside the store.
    :param create: The value to create new record tables for unknown symbols.
    :param add: The value to add the record row to the tables in the store.
    :param kwargs: Any keyword arguments for creating the record table objects.

    :return: The callback object.
    """

    async def wrapper(data: ModelIO) -> None:

        if not isinstance(data, tuple(callback.types)):
            return

        data: RecordRow

        for record in (
            store.get_all(data.signature) if data.signature in store else
            (
                store.add_all(
                    [
                        RecordTable(
                            exchange=data.exchange,
                            symbol=data.symbol,
                            **(kwargs or {})
                        )
                    ]
                ) if create else []
            )
        ):
            if add:
                record.append(data)

    callback = record_callback(wrapper)

    return callback

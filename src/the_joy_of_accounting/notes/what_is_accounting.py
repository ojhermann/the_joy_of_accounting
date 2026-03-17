from datetime import datetime
from decimal import Decimal
from typing import Collection, Protocol

from tool.interface.explicit import Immutable
from tool.interface.implicit import Hashable, TotalOrdering


class ID(Hashable, Immutable, TotalOrdering): ...


class Asset(Protocol):
    def id(self) -> ID: ...

    def description(self) -> str: ...

    def obligations(self) -> Collection[Obligation]:
        """
        Obligations that were used to fund the Asset
        """
        ...

    def timestamp(self) -> datetime: ...

    def value(self) -> Decimal: ...


class Obligation(Protocol):
    def id(self) -> ID: ...

    def description(self) -> str: ...

    def timestamp(self) -> datetime: ...

    def value(self) -> Decimal: ...


class BalanceSheet(Protocol):
    def assets(self) -> Collection[Asset]: ...

    def obligations(self) -> Collection[Obligation]: ...


class IncomeStatement(Protocol): ...


class CashFlowStatement(Protocol): ...

from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from typing import Collection, Optional, Protocol

from tool.interface.explicit import Immutable
from tool.interface.implicit import Hashable, TotalOrdering


class ID(Hashable, Immutable, TotalOrdering): ...


class Entity(Protocol):
    def id(self) -> ID: ...

    def description(self) -> str: ...

    def timestamp(self) -> datetime: ...

    def value(self) -> Decimal: ...


class Asset(Entity, Protocol):
    def obligations(self) -> Collection[Obligation]:
        """
        Obligations used to fund the Asset
        """
        ...


class Obligation(Entity, Protocol):
    def assets(self) -> Collection[Asset]:
        """
        Assets funded by the Obligations
        """
        ...


class Account(Protocol):
    def id(self) -> ID: ...

    def description(self) -> str: ...

    def timestamp(self) -> datetime: ...

    def type_of_entity(self) -> type[Entity]: ...


class ChartOfAccounts(Protocol):
    def by_id(self, account_id: ID) -> Optional[Account]: ...

    def by_type(self, t: type[Entity]) -> Collection[Account]: ...


class BalanceSheet(Protocol):
    def assets(self) -> Collection[Asset]: ...

    def obligations(self) -> Collection[Obligation]: ...

    def is_balanced(self) -> bool:
        return sum([a.value() for a in self.assets]) == sum(
            [o.value() for o in self.obligations]
        )


class IncomeStatement(Protocol): ...


class CashFlowStatement(Protocol): ...


class FinancialStatement(Protocol):
    def id(self) -> ID: ...

    def description(self) -> str: ...

    def timestamp(self) -> datetime: ...

    def balance_sheet(self) -> BalanceSheet: ...

    def income_statement(self) -> IncomeStatement: ...

    def cash_flow_statement(self) -> CashFlowStatement: ...


class MethodsOfValuingAssets(StrEnum):
    historical_cost = "how much a business paid for an asset"

    fair_value = "the fair price that a reasonable buyer and seller agree on"

    market_value = "the price that other people are currently paying for the same asset"

    realizable_value = "what you could expect to sell an asset for"

    current_cost = "how much you'd pay to replace the asset"

    replacement_cost = current_cost

    present_value = "the sum of all cash flows an asset would generate over a given time period, adjusted by some cost of capital"


class RecognitionCriteria(StrEnum):
    control = (
        "an asset must be controled by an entity to appear in that entity's accounts"
    )

    measurement = "an asset must be reliably measured to appear in an entity's accounts"

from datetime import datetime
from decimal import Decimal
from typing import Collection, Protocol


class Asset(Protocol):
    def description(self) -> str: ...

    def obligations(self) -> Collection[Obligation]:
        """
        Obligations that were used to fund the Asset
        """
        ...

    def timestamp(self) -> datetime: ...

    def value(self) -> Decimal: ...


class Obligation(Protocol):
    def timestamp(self) -> datetime: ...

    def value(self) -> Decimal: ...

from abc import ABC
from typing import TypeVar

T = TypeVar("T")


class Immutable(ABC):
    def __delattr__(self, name: str) -> None:
        raise AttributeError(
            f"{self.__class__.__name__} instances are immutable; {name} cannot be deleted"
        )

    def __setattr__(self, name: str, value: T) -> None:
        raise AttributeError(
            f"{self.__class__.__name__} instances are immutable; {name} cannot be changed"
        )

from typing import Protocol, Self


class Hashable(Protocol):
    def __hash__(self) -> int: ...


class TotalOrdering(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...

    def __eq__(self, other: object, /) -> bool: ...

    def __le__(self, other: Self, /) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: Self, /) -> bool:
        return not self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: Self, /) -> bool:
        return not self.__le__(other)

from functools import total_ordering
from typing import Self

import pytest

from tool.interface.implicit import TotalOrdering


@total_ordering
class Score:
    def __init__(self, value: int) -> None:
        self._value: int = value

    def __lt__(self, other: Self) -> bool:
        return self._value < other._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Score):
            return NotImplemented
        return self._value == other._value


class TestTotalOrderingInt:
    @pytest.mark.unit_test
    def test_lt(self) -> None:
        a: TotalOrdering = 1
        b: TotalOrdering = 2
        assert (a < b) is True
        assert (b < a) is False
        assert (a < a) is False

    @pytest.mark.unit_test
    def test_eq(self) -> None:
        a: TotalOrdering = 1
        b: TotalOrdering = 2
        assert (a == a) is True
        assert (a == b) is False

    @pytest.mark.unit_test
    def test_le(self) -> None:
        a: TotalOrdering = 1
        b: TotalOrdering = 2
        assert (a <= b) is True
        assert (a <= a) is True
        assert (b <= a) is False

    @pytest.mark.unit_test
    def test_ge(self) -> None:
        a: TotalOrdering = 1
        b: TotalOrdering = 2
        assert (b >= a) is True
        assert (a >= a) is True
        assert (a >= b) is False

    @pytest.mark.unit_test
    def test_gt(self) -> None:
        a: TotalOrdering = 1
        b: TotalOrdering = 2
        assert (b > a) is True
        assert (a > a) is False
        assert (a > b) is False


class TestTotalOrderingStr:
    @pytest.mark.unit_test
    def test_lt(self) -> None:
        a: TotalOrdering = "apple"
        b: TotalOrdering = "banana"
        assert (a < b) is True
        assert (b < a) is False
        assert (a < a) is False

    @pytest.mark.unit_test
    def test_eq(self) -> None:
        a: TotalOrdering = "apple"
        b: TotalOrdering = "banana"
        assert (a == a) is True
        assert (a == b) is False

    @pytest.mark.unit_test
    def test_le(self) -> None:
        a: TotalOrdering = "apple"
        b: TotalOrdering = "banana"
        assert (a <= b) is True
        assert (a <= a) is True
        assert (b <= a) is False

    @pytest.mark.unit_test
    def test_ge(self) -> None:
        a: TotalOrdering = "apple"
        b: TotalOrdering = "banana"
        assert (b >= a) is True
        assert (a >= a) is True
        assert (a >= b) is False

    @pytest.mark.unit_test
    def test_gt(self) -> None:
        a: TotalOrdering = "apple"
        b: TotalOrdering = "banana"
        assert (b > a) is True
        assert (a > a) is False
        assert (a > b) is False


class TestTotalOrderingScore:
    @pytest.mark.unit_test
    def test_lt(self) -> None:
        assert (Score(1) < Score(2)) is True
        assert (Score(2) < Score(1)) is False
        assert (Score(1) < Score(1)) is False

    @pytest.mark.unit_test
    def test_eq(self) -> None:
        assert (Score(1) == Score(1)) is True
        assert (Score(1) == Score(2)) is False

    @pytest.mark.unit_test
    def test_le(self) -> None:
        assert (Score(1) <= Score(2)) is True
        assert (Score(1) <= Score(1)) is True
        assert (Score(2) <= Score(1)) is False

    @pytest.mark.unit_test
    def test_ge(self) -> None:
        assert (Score(2) >= Score(1)) is True
        assert (Score(1) >= Score(1)) is True
        assert (Score(1) >= Score(2)) is False

    @pytest.mark.unit_test
    def test_gt(self) -> None:
        assert (Score(2) > Score(1)) is True
        assert (Score(1) > Score(1)) is False
        assert (Score(1) > Score(2)) is False

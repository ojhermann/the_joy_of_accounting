import pytest

from tool.interface.explicit import Immutable


class Point(Immutable):
    def __init__(self, x: int, y: int) -> None:
        self.x: int
        self.y: int
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)


@pytest.mark.unit_test
def test_instantiation() -> None:
    p = Point(1, 2)
    assert p.x == 1
    assert p.y == 2


@pytest.mark.unit_test
def test_setattr_raises() -> None:
    p = Point(1, 2)
    with pytest.raises(
        AttributeError, match="Point instances are immutable; x cannot be changed"
    ):
        p.x = 99


@pytest.mark.unit_test
def test_setattr_new_attribute_raises() -> None:
    p = Point(1, 2)
    with pytest.raises(
        AttributeError, match="Point instances are immutable; z cannot be changed"
    ):
        p.z = 0


@pytest.mark.unit_test
def test_delattr_raises() -> None:
    p = Point(1, 2)
    with pytest.raises(
        AttributeError, match="Point instances are immutable; x cannot be deleted"
    ):
        del p.x


@pytest.mark.unit_test
def test_error_message_includes_class_name() -> None:
    class Foo(Immutable):
        pass

    f = Foo()
    with pytest.raises(AttributeError, match="Foo instances are immutable"):
        f.bar = 1

import pytest

from rusty_utils import Option, Result, UnwrapError


def test_is_some() -> None:
    assert Option(42).is_some() is True
    assert Option().is_some() is False


def test_is_none() -> None:
    assert Option(42).is_none() is False
    assert Option().is_none() is True


def test_is_some_and() -> None:
    assert Option(42).is_some_and(lambda x: x > 0) is True
    assert Option(-1).is_some_and(lambda x: x > 0) is False
    assert Option().is_some_and(lambda x: x > 0) is False


def test_expect() -> None:
    assert Option(42).expect("Should not happen") == 42
    with pytest.raises(ValueError):
        Option().expect("Should happen")


def test_unwrap() -> None:
    assert Option(42).unwrap() == 42
    with pytest.raises(UnwrapError):
        Option().unwrap()


def test_unwrap_or() -> None:
    assert Option(42).unwrap_or(0) == 42
    assert Option().unwrap_or(0) == 0


def test_unwrap_or_else() -> None:
    assert Option(42).unwrap_or_else(lambda: 0) == 42
    assert Option().unwrap_or_else(lambda: 0) == 0


def test_map() -> None:
    assert Option(42).map(lambda x: x * 2) == Option(84)
    assert Option().map(lambda x: x * 2) == Option()


def test_map_or() -> None:
    assert Option(42).map_or(0, lambda x: x * 2) == 84
    assert Option().map_or(0, lambda x: x * 2) == 0


def test_map_or_else() -> None:
    assert Option(42).map_or_else(lambda: 0, lambda x: x * 2) == 84
    assert Option().map_or_else(lambda: 0, lambda x: x * 2) == 0


def test_inspect() -> None:
    def side_effect(_: object) -> None:
        pass

    assert Option(42).inspect(side_effect) == Option(42)
    assert Option().inspect(side_effect) == Option()


def test_ok_or() -> None:
    assert Option(42).ok_or(ValueError("Error")) == Result(ok=42)
    assert Option().ok_or(ValueError("Error")) == Result(err=ValueError("Error"))


def test_ok_or_else() -> None:
    assert Option(42).ok_or_else(lambda: ValueError("Error")) == Result(ok=42)
    assert Option().ok_or_else(lambda: ValueError("Error")) == Result(err=ValueError("Error"))


def test_and_() -> None:
    assert Option(42).and_(Option("foo")) == Option("foo")
    assert Option().and_(Option("foo")) == Option()


def test_and_then() -> None:
    assert Option(42).and_then(lambda x: Option(x * 2)) == Option(84)
    assert Option().and_then(lambda x: Option(x * 2)) == Option()


def test_or_() -> None:
    assert Option(42).or_(Option(0)) == Option(42)
    assert Option().or_(Option(0)) == Option(0)


def test_or_else() -> None:
    assert Option(42).or_else(lambda: Option(0)) == Option(42)
    assert Option().or_else(lambda: Option(0)) == Option(0)


def test_xor() -> None:
    assert Option(42).xor(Option()) == Option(42)
    assert Option().xor(Option(42)) == Option(42)
    assert Option(42).xor(Option(42)) == Option()
    assert Option().xor(Option()) == Option()

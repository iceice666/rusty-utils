import pytest

from rusty_utils import Result, UnwrapError
from rusty_utils.result import Catch


class TestException(Exception):
    __test__ = False

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TestException)


def get_exception(msg: str = "Error occurred") -> TestException:
    return TestException(msg)


ResT = Result[int, TestException]


def test_ok_value() -> None:
    result: ResT = Result(ok=42)
    assert result.is_ok() is True
    assert result.is_err() is False
    assert result.ok_value == 42


def test_err_value() -> None:
    result: ResT = Result(err=get_exception())
    assert result.is_ok() is False
    assert result.is_err() is True
    assert result.err_value == get_exception()


def test_invalid_initialization() -> None:
    with pytest.raises(ValueError):
        Result(ok=42, err=get_exception())
    with pytest.raises(ValueError):
        Result()


def test_ok_method() -> None:
    result: ResT = Result(ok=42)
    assert result.ok().is_some() is True
    assert result.ok().unwrap() == 42


def test_err_method() -> None:
    result: ResT = Result(err=get_exception())
    assert result.err().is_some() is True
    assert result.err().unwrap() == get_exception()


def test_map_ok_value() -> None:
    result: ResT = Result(ok=2)
    new_result = result.map(lambda x: x * 2)
    assert new_result.is_ok() is True
    assert new_result.ok_value == 4


def test_map_err_value() -> None:
    result: ResT = Result(err=get_exception())
    new_result = result.map(lambda x: x * 2)
    assert new_result.is_err() is True
    assert new_result.err_value == get_exception()


def test_map_err() -> None:
    def map_err(_: Exception) -> Exception:
        return get_exception("Error occurred again")

    result: ResT = Result(err=get_exception())
    new_result = result.map_err(map_err)
    assert new_result.is_err() is True
    assert new_result.err_value == get_exception("Error occurred again")


def test_map_or() -> None:
    result_ok: ResT = Result(ok=10)
    result_err: ResT = Result(err=get_exception())
    assert result_ok.map_or(5, lambda x: x * 2) == 20
    assert result_err.map_or(5, lambda x: x * 2) == 5


def test_map_or_else() -> None:
    result_ok: ResT = Result(ok=10)
    result_err: ResT = Result(err=get_exception())
    assert result_ok.map_or_else(lambda e: 5, lambda x: x * 2) == 20
    assert result_err.map_or_else(lambda e: 5, lambda x: x * 2) == 5


def test_unwrap_ok() -> None:
    result: ResT = Result(ok=42)
    assert result.unwrap() == 42


def test_unwrap_err() -> None:
    result: ResT = Result(err=get_exception())
    with pytest.raises(UnwrapError):
        result.unwrap()


def test_unwrap_or() -> None:
    result_ok: ResT = Result(ok=42)
    result_err: ResT = Result(err=get_exception())
    assert result_ok.unwrap_or(100) == 42
    assert result_err.unwrap_or(100) == 100


def test_unwrap_or_else() -> None:
    result_ok: ResT = Result(ok=42)
    result_err: ResT = Result(err=get_exception())
    assert result_ok.unwrap_or_else(lambda e: 100) == 42
    assert result_err.unwrap_or_else(lambda e: 100) == 100


def test_expect() -> None:
    result: ResT = Result(ok=42)
    assert result.expect("Should not raise error") == 42


def test_expect_err() -> None:
    result: ResT = Result(err=get_exception())
    with pytest.raises(UnwrapError):
        result.expect("Error occurred")


def test_and_ok() -> None:
    result1: ResT = Result(ok=10)
    result2: ResT = Result(ok=20)
    assert result1.and_(result2).unwrap() == 20


def test_and_err() -> None:
    result1: ResT = Result(err=get_exception())
    result2: ResT = Result(ok=20)
    assert result1.and_(result2).is_err() is True


def test_or_ok() -> None:
    result1: ResT = Result(ok=10)
    result2: ResT = Result(ok=20)
    assert result1.or_(result2).unwrap() == 10


def test_or_err() -> None:
    result1: ResT = Result(err=get_exception())
    result2: ResT = Result(ok=20)
    assert result1.or_(result2).unwrap() == 20


def test_catch() -> None:
    result_ok: Result[float, TestException] = Catch(lambda: 42 / 2, TestException)
    assert result_ok.is_ok() is True
    assert result_ok.unwrap() == 21

    result_err: Result[float, ZeroDivisionError] = Catch(lambda: 42 / 0, ZeroDivisionError)
    assert result_err.is_err() is True
    with pytest.raises(ZeroDivisionError):
        raise result_err.unwrap_err()

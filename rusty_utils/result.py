import inspect
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable, TYPE_CHECKING, ParamSpec, Union, overload

if TYPE_CHECKING:
    from rusty_utils.option import Option

from rusty_utils.common import UnwrapError

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E", bound=BaseException)
F = TypeVar("F", bound=BaseException)
P = ParamSpec("P")


@dataclass(frozen=True)
class Ok(Generic[T, E]):
    """
    Represents a successful `Result` with an `Ok` value.
    
    Attributes:
        value (T): The value held in a successful `Result`.
    """

    value: T

    def is_ok(self) -> bool:
        """Checks if the `Result` is an `Ok` value."""
        return True

    def is_err(self) -> bool:
        """Checks if the `Result` is an `Err` value."""
        return False

    def ok(self) -> "Option[T]":
        """Retrieves the `Ok` value."""
        from rusty_utils.option import Option
        return Option(self.value)

    def err(self) -> "Option[E]":
        """Retrieves the `Err` value, which in this case is `None` since it's an `Ok`."""
        from rusty_utils.option import Option
        return Option(None)

    def map(self, f: Callable[[T], U]) -> "Result[U, E]":
        """Transforms the `Ok` value using the provided function."""
        return Ok(f(self.value))

    def map_or(self, default: U, f: Callable[[T], U]) -> U:
        """Transforms the `Ok` value using the function or returns a default if `Err`."""
        return f(self.value)

    def map_or_else(self, f_err: Callable[[E], U], f_ok: Callable[[T], U]) -> U:
        """Transforms the `Ok` value using the provided function."""
        return f_ok(self.value)

    def map_err(self, f: Callable[[E], F]) -> "Result[T, F]":
        """Passes through the `Ok` value without transforming the `Err`."""
        return Ok(self.value)

    def expect(self, msg: str) -> T:
        """
        Unwraps the `Ok` value or raises an `UnwrapError` with the provided message if the result is an `Err`.
        
        Args:
            msg (str): Error message for an `Err` result.
        
        Returns:
            T: The `Ok` value.
        """
        return self.value

    def expect_err(self, msg: str) -> E:
        """
        Raises an `UnwrapError` because this is an `Ok` value.
        
        Args:
            msg (str): The error message.
        
        Raises:
            UnwrapError: Always raises an error because this is an `Ok`.
        """
        raise UnwrapError(msg)

    def unwrap(self) -> T:
        """Unwraps the `Ok` value."""
        return self.value

    def unwrap_err(self) -> E:
        """Raises an `UnwrapError` because this is an `Ok` value."""
        raise UnwrapError(f"Called 'unwrap_err' on an `Ok` value: {self.value}")

    def unwrap_or(self, default: T) -> T:
        """Returns the `Ok` value."""
        return self.value

    def unwrap_or_else(self, f: Callable[[E], T]) -> T:
        """Returns the `Ok` value."""
        return self.value

    def unwrap_or_raise(self) -> T:
        """Unwraps the `Ok` value."""
        return self.value

    def and_(self, other: "Result[U, E]") -> "Result[U, E]":
        """
        Returns the provided `Result` if this `Result` is `Ok`, otherwise returns the current `Err`.
        
        Args:
            other (Result[U, E]): A `Result` object to return if this is an `Ok`.
        
        Returns:
            Result[U, E]: The provided `Result` or the current `Err`.
        """
        return other

    def or_(self, other: "Result[T, F]") -> "Result[T, F]":
        """
        Returns the current `Ok` value or the provided `Result` if this is an `Err`.
        
        Args:
            other (Result[T, F]): A `Result` object to return if this is an `Err`.
        
        Returns:
            Result[T, F]: The current `Ok` value or the provided `Result`.
        """
        return Ok(self.value)

    def __repr__(self) -> str:
        return f"Ok({self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ok):
            return False

        return bool(self.value == other.value)


@dataclass(frozen=True)
class Err(Generic[T, E]):
    """
    Represents a failed `Result` with an `Err` value.
    
    Attributes:
        value (E): The error contained in the `Err`.
    """

    value: E

    def is_ok(self) -> bool:
        """Checks if the `Result` is an `Ok` value."""
        return False

    def is_err(self) -> bool:
        """Checks if the `Result` is an `Err` value."""
        return True

    def ok(self) -> "Option[T]":
        """Retrieves the `Ok` value, which is `None` in this case."""
        from rusty_utils.option import Option
        return Option(None)

    def err(self) -> "Option[E]":
        """Retrieves the `Err` value."""
        from rusty_utils.option import Option
        return Option(self.value)

    def map(self, f: Callable[[T], U]) -> "Result[U, E]":
        """Passes through the `Err` value without transforming it."""
        return Err(self.value)

    def map_or(self, default: U, f: Callable[[T], U]) -> U:
        """Returns the default value as this is an `Err`."""
        return default

    def map_or_else(self, f_err: Callable[[E], U], f_ok: Callable[[T], U]) -> U:
        """Transforms the `Err` value using the provided function."""
        return f_err(self.value)

    def map_err(self, f: Callable[[E], F]) -> "Result[T, F]":
        """Transforms the `Err` value using the provided function."""
        return Err(f(self.value))

    def expect(self, msg: str) -> T:
        """
        Raises an `UnwrapError` with the provided message because this is an `Err`.
        
        Args:
            msg (str): Error message for unwrapping.
        
        Raises:
            UnwrapError: Always raises an error since this is an `Err`.
        """
        raise UnwrapError(msg)

    def expect_err(self, msg: str) -> E:
        """
        Unwraps the `Err` value or raises an `UnwrapError` with the provided message if the result is an `Ok`.
        
        Args:
            msg (str): Error message for unwrapping an `Ok` value.
        
        Returns:
            E: The `Err` value.
        """
        return self.value

    def unwrap(self) -> T:
        """Raises an `UnwrapError` because this is an `Err` value."""
        raise UnwrapError(f"Called 'unwrap' on an `Err` value: {self.value}")

    def unwrap_err(self) -> E:
        """Unwraps the `Err` value."""
        return self.value

    def unwrap_or(self, default: T) -> T:
        """Returns the default value since this is an `Err`."""
        return default

    def unwrap_or_else(self, f: Callable[[E], T]) -> T:
        """Computes a default from the `Err` value."""
        return f(self.value)

    def unwrap_or_raise(self) -> T:
        """Raises the `Err` value since this is an error."""
        raise self.value

    def and_(self, other: "Result[U, E]") -> "Result[U, E]":
        """
        Returns the provided `Result` if this `Result` is `Ok`, otherwise returns the current `Err`.
        
        Args:
            other (Result[U, E]): A `Result` object to return if this is an `Ok`.
        
        Returns:
            Result[U, E]: The provided `Result` or the current `Err`.
        """
        return Err(self.value)

    def or_(self, other: "Result[T, F]") -> "Result[T, F]":
        """
        Returns the current `Ok` value or the provided `Result` if this is an `Err`.
        
        Args:
            other (Result[T, F]): A `Result` object to return if this is an `Err`.
        
        Returns:
            Result[T, F]: The provided `Result` or the current `Err`.
        """
        return other

    def __repr__(self) -> str:
        return f"Err({self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Err):
            return False

        return str(self.value) == str(other.value)


Result = Union[Ok[T, E], Err[T, E]]


# Decorator
@overload
def Catch(*err_type: type[E]) -> Callable[[Callable[P, T]], Callable[P, "Result[T, E]"]]: ...


# Direct call
@overload
def Catch(*err_type: type[E], func: Callable[P, T]) -> "Result[T, E]": ...


def Catch(*err_type: type[E], func: Optional[Callable[P, T]] = None) -> Union[
    Callable[[Callable[P, T]], Callable[P, "Result[T, E]"]],
    "Result[T, E]"
]:
    """
    A decorator that captures exceptions and returns a `Result`.
    
    If an exception occurs, it returns an `Err` containing the exception; 
    otherwise, it returns an `Ok` containing the function's result.
    
    Args:
        err_type (type[E]): One or more exception types to catch.
        func (Callable[P, T]): The function to execute.
    
    Returns:
        Either a `Result` containing `Ok` if the function executes without exception, or an `Err`.
    """
    from functools import wraps

    if not err_type or not all(inspect.isclass(e) and issubclass(e, BaseException) for e in err_type):
        raise TypeError("Catch decorator requires at least one exception type")

    if func is None:
        def decorator(f: Callable[P, T]) -> Callable[P, "Result[T, E]"]:
            @wraps(f)
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> "Result[T, E]":
                try:
                    return Ok(f(*args, **kwargs))
                except err_type as e:
                    return Err(e)

            return wrapper

        return decorator
    else:
        try:
            return Ok(func())
        except err_type as e:
            return Err(e)

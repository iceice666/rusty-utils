from dataclasses import dataclass
from typing import TypeVar, Callable, Generic

from rusty_utils.common import UnwrapError

T = TypeVar('T')
U = TypeVar('U')
E = TypeVar('E', bound=Exception)


@dataclass(frozen=True)
class Option(Generic[T]):
    """A class that expands the built-in Optional type, representing a value that may or may not be present (Some or None).

    Attributes:
        value (T | None): The value stored in the option or None if no value.
    """
    value: T | None = None

    def __init__(self, value: T | None = None):
        """Initialize the Option class with an optional value.

        Args:
            value (T | None): The value to be stored in the Option, or None if absent.
        """
        object.__setattr__(self, 'value', value)

    def __repr__(self) -> str:
        """String representation of the Option instance.

        Returns:
            str: "None" if no value is present, otherwise "Some(value)".
        """
        return "None" if self.value is None else f"Some({self.value})"

    def is_some(self) -> bool:
        """Check if the Option contains a value.

        Returns:
            bool: True if the option contains a value, False otherwise.
        """
        return self.value is not None

    def is_none(self) -> bool:
        """Check if the Option contains no value.

        Returns:
            bool: True if the option contains no value, False otherwise.
        """
        return self.value is None

    def is_some_and(self, f: Callable[[T], bool]) -> bool:
        """Check if the Option contains a value and the predicate returns True.

        Args:
            f (Callable[[T], bool]): A function that takes the value and returns a bool.

        Returns:
            bool: True if the Option contains a value and the predicate is True, False otherwise.
        """
        return self.is_some() and f(self.value)

    def expect(self, message: str) -> T:
        """Return the contained value or raise a ValueError with the provided message if None.

        Args:
            message (str): The message for the error if the Option contains no value.

        Returns:
            T: The contained value.

        Raises:
            ValueError: If the Option contains no value.
        """
        if self.value is not None:
            return self.value
        else:
            raise ValueError(message)

    def unwrap(self) -> T:
        """Return the contained value or raise an UnwrapError if None.

        Returns:
            T: The contained value.

        Raises:
            UnwrapError: If the Option contains no value.
        """
        if self.value is not None:
            return self.value
        else:
            raise UnwrapError("Option is None")

    def unwrap_or(self, default: T) -> T:
        """Return the contained value or the provided default if None.

        Args:
            default (T): The default value to return if the Option contains no value.

        Returns:
            T: The contained value or the default.
        """
        return self.value if self.value is not None else default

    def unwrap_or_else(self, f: Callable[[], T]) -> T:
        """Return the contained value or the result of the provided function if None.

        Args:
            f (Callable[[], T]): A function that returns a value to be used if the Option contains no value.

        Returns:
            T: The contained value or the result of the function.
        """
        return self.value if self.value is not None else f()

    def map(self, f: Callable[[T], U]) -> 'Option[U]':
        """Apply a function to the contained value and return a new Option containing the result.

        Args:
            f (Callable[[T], U]): A function that takes the contained value and returns a new value.

        Returns:
            Option[U]: A new Option with the result of the function or None if the original Option was None.
        """
        return Option(f(self.value)) if self.value is not None else Option()

    def map_or(self, default: U, f: Callable[[T], U]) -> U:
        """Apply a function to the contained value or return the provided default if None.

        Args:
            default (U): The default value to return if the Option contains no value.
            f (Callable[[T], U]): A function that takes the contained value and returns a new value.

        Returns:
            U: The result of the function or the default value.
        """
        return f(self.value) if self.value is not None else default

    def map_or_else(self, default_f: Callable[[], U], f: Callable[[T], U]) -> U:
        """Apply a function to the contained value or return the result of a default function if None.

        Args:
            default_f (Callable[[], U]): A function that returns a default value if the Option contains no value.
            f (Callable[[T], U]): A function that takes the contained value and returns a new value.

        Returns:
            U: The result of the function or the result of the default function.
        """
        return f(self.value) if self.value is not None else default_f()

    def inspect(self, f: Callable[[T], None]) -> 'Option[T]':
        """Call a function with the contained value for side effects and return the Option unchanged.

        Args:
            f (Callable[[T], None]): A function that takes the contained value for side effects.

        Returns:
            Option[T]: The original Option.
        """
        if self.value is not None:
            f(self.value)
        return self

    def ok_or(self, err: E) -> "Result[T, E]":
        """Convert the Option to a Result, returning Ok(value) if Some, or Err(err) if None.

        Args:
            err (E): The error to return if the Option contains no value.

        Returns:
            Result[T, E]: Ok with the value if Some, Err with the error if None.
        """
        from rusty_utils.result import Result
        return Result(ok=self.value) if self.value is not None else Result(err=err)

    def ok_or_else(self, err_f: Callable[[], E]) -> "Result[T, E]":
        """Convert the Option to a Result, returning Ok(value) if Some, or Err from a function if None.

        Args:
            err_f (Callable[[], E]): A function that returns an error if the Option contains no value.

        Returns:
            Result[T, E]: Ok with the value if Some, Err with the result of the function if None.
        """
        from rusty_utils.result import Result
        return Result(ok=self.value) if self.value is not None else Result(err=err_f())

    def and_(self, optb: 'Option[U]') -> 'Option[U]':
        """Return the second Option if the first is Some, otherwise return None.

        Args:
            optb (Option[U]): The second Option to return if the first is Some.

        Returns:
            Option[U]: The second Option if the first is Some, otherwise None.
        """
        return optb if self.value is not None else Option()

    def and_then(self, f: Callable[[T], 'Option[U]']) -> 'Option[U]':
        """Call a function if the Option is Some and return its result, otherwise return None.

        Args:
            f (Callable[[T], Option[U]]): A function that takes the contained value and returns a new Option.

        Returns:
            Option[U]: The result of the function if Some, otherwise None.
        """
        return f(self.value) if self.value is not None else Option()

    def or_(self, optb: 'Option[T]') -> 'Option[T]':
        """Return the first Option if it's Some, otherwise return the second Option.

        Args:
            optb (Option[T]): The second Option to return if the first is None.

        Returns:
            Option[T]: The first Option if it's Some, otherwise the second Option.
        """
        return self if self.value is not None else optb

    def or_else(self, f: Callable[[], 'Option[T]']) -> 'Option[T]':
        """Return the first Option if it's Some, otherwise return the result of a function.

        Args:
            f (Callable[[], Option[T]]): A function that returns a new Option if the first is None.

        Returns:
            Option[T]: The first Option if it's Some, otherwise the result of the function.
        """
        return self if self.value is not None else f()

    def xor(self, optb: 'Option[T]') -> 'Option[T]':
        """Return Some if exactly one of the options is Some, otherwise return None.

        Args:
            optb (Option[T]): The other Option to compare with.

        Returns:
            Option[T]: Some if exactly one of the options is Some, otherwise None.
        """
        if self.is_some() and optb.is_none():
            return self
        elif self.is_none() and optb.is_some():
            return optb
        else:
            return Option()

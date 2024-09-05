from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

from rusty_utils.common import UnwrapError

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E", bound=Exception)
F = TypeVar("F", bound=Exception)


@dataclass(frozen=True)
class Result(Generic[T, E]):
    """
    A generic container that represents either success ('Ok' value) or failure ('Err' value).

    Attributes:
        ok_value: The value contained if the Result is successful.
        err_value: The error contained if the Result is a failure.
        __is_ok__: A boolean indicating whether the result is 'Ok' (True) or 'Err' (False).
    """

    ok_value: T
    err_value: E
    __is_ok__: bool

    def __init__(self, ok: Optional[T] = None, err: Optional[E] = None):
        """
        Initializes a Result object with either an 'ok_value' or an 'err_value'.

        Args:
            ok: The value representing success.
            err: The value representing failure.

        Raises:
            ValueError: If both or neither ok_value and err_value are provided.
        """
        if ok is not None and err is not None:
            raise ValueError("Either ok_value or err_value must be provided, not both")
        elif ok is not None:
            object.__setattr__(self, "ok_value", ok)
            object.__setattr__(self, "__is_ok__", True)
        elif err is not None:
            object.__setattr__(self, "err_value", err)
            object.__setattr__(self, "__is_ok__", False)
        else:
            raise ValueError("Either ok_value or err_value must be provided")

    def is_ok(self) -> bool:
        """
        Checks if the Result is an 'Ok' value.

        Returns:
            True if the Result is 'Ok', otherwise False.
        """
        return self.__is_ok__

    def is_err(self) -> bool:
        """
        Checks if the Result is an 'Err' value.

        Returns:
            True if the Result is 'Err', otherwise False.
        """
        return not self.__is_ok__

    def ok(self) -> "Option[T]":
        """
        Retrieves the 'Ok' value if the Result is successful.

        Returns:
            The 'Ok' value if present, otherwise None.
        """
        from rusty_utils.option import Option
        return Option(self.ok_value) if self.__is_ok__ else Option()

    def err(self) -> "Option[E]":
        """
        Retrieves the 'Err' value if the Result is a failure.

        Returns:
            The 'Err' value if present, otherwise None.
        """
        from rusty_utils.option import Option
        return Option(self.err_value) if not self.__is_ok__ else Option()

    def map(self, f: Callable[[T], U]) -> "Result[U, E]":
        """
        Transforms the 'Ok' value using the provided function.

        Args:
            f: A function to apply to the 'Ok' value.

        Returns:
            A new Result with the transformed 'Ok' value, or the original 'Err' value if applicable.
        """
        return Result(ok=f(self.ok_value)) if self.__is_ok__ else Result(err=self.err_value)

    def map_or(self, default: U, f: Callable[[T], U]) -> U:
        """
        Transforms the 'Ok' value or returns the default if the Result is an error.

        Args:
            default: The default value to return if the Result is an 'Err'.
            f: A function to apply to the 'Ok' value.

        Returns:
            The transformed 'Ok' value or the default value if the Result is an 'Err'.
        """
        return f(self.ok_value) if self.__is_ok__ else default

    def map_or_else(self, f_err: Callable[[E], U], f_ok: Callable[[T], U]) -> U:
        """
        Transforms the 'Ok' or 'Err' value using the provided functions based on the Result's state.

        Args:
            f_err: A function to apply to the 'Err' value.
            f_ok: A function to apply to the 'Ok' value.

        Returns:
            The result of applying 'f_ok' to the 'Ok' value or 'f_err' to the 'Err' value.
        """
        return f_ok(self.ok_value) if self.__is_ok__ else f_err(self.err_value)

    def map_err(self, f: Callable[[E], F]) -> "Result[T, F]":
        """
        Transforms the 'Err' value using the provided function.

        Args:
            f: A function to apply to the 'Err' value.

        Returns:
            A new Result with the transformed 'Err' value, or the original 'Ok' value if applicable.
        """
        return Result(ok=self.ok_value) if self.__is_ok__ else Result(err=f(self.err_value))

    def inspect(self, f: Callable[[T], None]) -> "Result[T, E]":
        """
        Executes the provided function on the 'Ok' value without transforming it.

        Args:
            f: A function to apply to the 'Ok' value.

        Returns:
            The original Result object.
        """
        if self.__is_ok__:
            f(self.ok_value)
        return self

    def inspect_err(self, f: Callable[[E], None]) -> "Result[T, E]":
        """
        Executes the provided function on the 'Err' value without transforming it.

        Args:
            f: A function to apply to the 'Err' value.

        Returns:
            The original Result object.
        """
        if not self.__is_ok__:
            f(self.err_value)
        return self

    def expect(self, msg: str) -> T:
        """
        Unwraps the 'Ok' value or raises an UnwrapError with the provided message if the Result is an 'Err'.

        Args:
            msg: The error message to use if the Result is an 'Err'.

        Returns:
            The 'Ok' value if present.

        Raises:
            UnwrapError: If the Result is an 'Err'.
        """
        if self.__is_ok__:
            return self.ok_value
        else:
            raise UnwrapError(msg)

    def expect_err(self, msg: str) -> E:
        """
        Unwraps the 'Err' value or raises an UnwrapError with the provided message if the Result is an 'Ok'.

        Args:
            msg: The error message to use if the Result is an 'Ok'.

        Returns:
            The 'Err' value if present.

        Raises:
            UnwrapError: If the Result is an 'Ok'.
        """
        if self.__is_ok__:
            raise UnwrapError(msg)
        else:
            return self.err_value

    def unwrap(self) -> T:
        """
        Unwraps the 'Ok' value, or raises an UnwrapError if the Result is an 'Err'.

        Returns:
            The 'Ok' value if present.

        Raises:
            UnwrapError: If the Result is an 'Err'.
        """
        if self.__is_ok__:
            return self.ok_value
        else:
            raise UnwrapError(f"Called 'unwrap' on an 'Err' value: {self.err_value}")

    def unwrap_err(self) -> E:
        """
        Unwraps the 'Err' value, or raises an UnwrapError if the Result is an 'Ok'.

        Returns:
            The 'Err' value if present.

        Raises:
            UnwrapError: If the Result is an 'Ok'.
        """
        if self.__is_ok__:
            raise UnwrapError(f"Called 'unwrap_err' on an 'Ok' value: {self.ok_value}")
        else:
            return self.err_value

    def unwrap_or(self, default: T) -> T:
        """
        Returns the 'Ok' value or a default value if the Result is an 'Err'.

        Args:
            default: The value to return if the Result is an 'Err'.

        Returns:
            The 'Ok' value or the provided default value.
        """
        return self.ok_value if self.__is_ok__ else default

    def unwrap_or_else(self, f: Callable[[E], T]) -> T:
        """
        Returns the 'Ok' value or computes a default from the 'Err' value using the provided function.

        Args:
            f: A function to compute a value from the 'Err' value.

        Returns:
            The 'Ok' value or the result of applying 'f' to the 'Err' value.
        """
        return self.ok_value if self.__is_ok__ else f(self.err_value)

    def and_(self, other: "Result[U, E]") -> "Result[U, E]":
        """
        Returns the provided Result if this Result is 'Ok', otherwise returns the current 'Err'.

        Args:
            other: A Result object to return if this is an 'Ok'.

        Returns:
            The provided 'Result' or the current 'Err'.
        """
        return other if self.__is_ok__ else Result(err=self.err_value)

    def and_then(self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
        """
        Calls the provided function with the 'Ok' value if this is an 'Ok' Result.

        Args:
            f: A function to apply to the 'Ok' value.

        Returns:
            A new Result produced by the function, or the current 'Err' if this is an 'Err'.
        """
        return f(self.ok_value) if self.__is_ok__ else Result(err=self.err_value)

    def or_(self, other: "Result[T, F]") -> "Result[T, F]":
        """
        Returns the current 'Ok' value or the provided Result if this is an 'Err'.

        Args:
            other: A Result object to return if this is an 'Err'.

        Returns:
            The current 'Ok' value or the provided 'Result'.
        """
        return Result(ok=self.ok_value) if self.__is_ok__ else other

    def or_else(self, f: Callable[[E], "Result[T, F]"]) -> "Result[T, F]":
        """
        Calls the provided function with the 'Err' value if this is an 'Err' Result.

        Args:
            f: A function to apply to the 'Err' value.

        Returns:
            A new Result produced by the function, or the current 'Ok' value if this is an 'Ok'.
        """
        return Result(ok=self.ok_value) if self.__is_ok__ else f(self.err_value)

    def __repr__(self) -> str:
        if self.__is_ok__:
            return f"Ok({self.ok_value})"
        else:
            return f"Err({self.err_value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Result):
            return False

        if self.is_ok() and other.is_ok():
            return bool(self.ok_value == other.ok_value)
        elif self.is_err() and other.is_err():
            return isinstance(self.err_value, type(other.err_value)) and str(self.err_value) == str(other.err_value)
        return False

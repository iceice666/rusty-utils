# rusty-utils

Bringing useful tools from Rust to Python.

## 🚪 Portals

- [🚪 Portals](#-portals)
- [📥 Installation](#-installation)
- [📚 Features](#-features)
    - [Result\[T, E\]](#resultt-e)
    - [Option\[T\]](#optiont)
- [⚙️ Usage Examples](#️-usage-examples)
    - [Example: Handling API Responses](#example-handling-api-responses)
    - [Example: Safely Unwrapping Values](#example-safely-unwrapping-values)

## 📥 Installation

`rusty-utils` is available on [PyPI](https://pypi.org/project/rusty-utils/).

Install using `pip`:

```bash
pip install rusty-utils
```

Or with `poetry`:

```bash
poetry add rusty-utils
```

## 📚 Features

`rusty-utils` brings Rust-inspired constructs like `Result` and `Option` to Python, allowing developers to write cleaner
and more robust error-handling code.

For more details, check out the full [documentation](./docs/README.md).

### Result[T, E]

The `Result` type is inspired by Rust, enabling you to handle success (`Ok`) and failure (`Err`) in a clean, expressive
way.

```python
from rusty_utils import Result, Ok, Err

# Success case
success: Result[int, Exception] = Ok(42)

# Failure case
failure: Result[int, Exception] = Err(Exception("An error occurred"))
```

#### Custom Result Types

You can alias your own custom `Result` types to suit your domain-specific needs.

```python
from typing import TypeVar
from rusty_utils import Result, Ok, Err


class MyError(Exception): pass


_T = TypeVar("_T")
MyResult = Result[_T, MyError]

# Custom success and failure cases
success: MyResult[int] = Ok(42)
failure: MyResult[int] = Err(MyError("Something went wrong"))
```

#### `?` Operator

In Rust, the `?` operator is used to easily propagate errors up the call stack, allowing you to return early if a
function fails, and to handle success (`Ok`) and failure (`Err`) values concisely.

```rust
fn side_effect() -> Resut<i32, Error> {
    // some code that may fail
    Ok(42)
}

fn process() -> Result<(), Error> {
  let result = side_effect()?; // Propagates the error if it occurs
  ... // Other operation
}
```

In Python, you can't overload the `?` operator (we even didn't treat `?` as a valid operator in Python)

```python
result = side_effect()?  # What???
```

In Python, something has similar ability to *throw the `Err`* and remain the `Ok` value is:  
***Python built-in `try-except`***.

```python
from rusty_utils import Catch


def side_effect() -> float:
    # Simulate a potential failure (e.g., division by zero)
    return 42 / 0


@Catch(Exception, ZeroDivisionError)
def wrapped_side_effect() -> float:
    return side_effect()


@Catch(Exception)
def process() -> None:
    result1 = wrapped_side_effect().unwrap_or_raise()  # You achieve same functionality with `unwrap_or_raise()`!
    result2 = Catch(Exception, ZeroDivisionError, func=side_effect).unwrap_or_raise() 
```

In this example:

- We use the `@Catch(Exception)` decorator to make sure we can capture the raised `Err` and return to the caller.
    - What the `@Catch(E)` do is transform the function into a capturer which returns `Result[T, E]`
- We can use the `Catch` in this way (result2) to capture the result of a fallible function call into a `Result`.
- The `wrapped_side_effect()` function returns a `Result` that might be an error (`Err`) or a valid value (`Ok`).
    - Since the function returns a `float` and we mark it might raise an `Exception`, so it actually returns a
      `Result[float, Exception]`.
- Then use `unwrap_or_raise()` to handle the result: if it's an error, it raises the exception, effectively mimicking
  Rust's `?` operator.

This approach enables cleaner error propagation and handling in Python, much like in Rust, but using Python’s
exception-handling style.

> Although the `@Catch` decorator accpets multiple exception types, it's recommended to use it only for one type of
> exception at a time, or your linter might can't resolve the type hints correctly. (like it might think the
> `wrapped_side_effect` returns a `Result[float, Any]`)

#### API Overview

- **Querying Result Type:**
    - `is_ok()`: Returns `True` if the `Result` is `Ok`.
    - `is_err()`: Returns `True` if the `Result` is `Err`.

- **Unwrapping Values:**
    - `expect(message)`: Unwraps the value or raises `UnwrapError` with a custom message.
    - `unwrap()`: Unwraps the value or raises `UnwrapError`.
    - `unwrap_or(default)`: Returns the provided default value if `Err`.
    - `unwrap_or_else(func)`: Returns the result of the provided function if `Err`.
    - `unwrap_or_raise()`: Raises the exception contained in `Err`.

- **Transforming Results:**
    - `ok()`: Transforms `Ok` to `Option[T]`
    - `err()`: Transforms `Err` to `Option[E]`
    - `map(func)`: Applies `func` to the `Ok` value.
    - `map_err(func)`: Applies `func` to the `Err` value.
    - `map_or(default, func)`: Applies `func` to `Ok` or returns `default` if `Err`.
    - `map_or_else(f_err, f_ok)`: Applies different functions depending on whether the `Result` is `Ok` or `Err`.

- **Logical Operations:**
    - `and_(other)`: Returns the second `Result` if the first is `Ok`; otherwise returns the original `Err`.
    - `or_(other)`: Returns the first `Ok`, or the second `Result` if the first is `Err`.
    - `and_then(func)`: Chains another operation based on the `Ok` value.
    - `or_else(func)`: Chains another operation based on the `Err` value.

### Option[T]

The `Option` type expands Python's `Optional`, representing a value that may or may not be present (`Some` or `None`).

```python
from rusty_utils import Option

some_value: Option[int] = Option(42)
none_value: Option[int] = Option()
```

#### API Overview

- **Querying Option Type:**
    - `is_some()`: Returns `True` if the `Option` contains a value.
    - `is_none()`: Returns `True` if the `Option` contains no value.

- **Unwrapping Values:**
    - `expect(message)`: Unwraps the value or raises `UnwrapError` with a custom message.
    - `unwrap()`: Unwraps the value or raises `UnwrapError`.
    - `unwrap_or(default)`: Returns the provided default value if `None`.
    - `unwrap_or_else(func)`: Returns the result of a provided function if `None`.

- **Transforming Options:**
    - `map(func)`: Transforms the `Some` value.
    - `map_or(default, func)`: Transforms the `Some` value or returns a default if `None`.
    - `map_or_else(default_func, func)`: Transforms the `Some` value or returns the result of a default function if
      `None`.

- **Logical Operations:**
    - `and_(other)`: Returns the second `Option` if the first is `Some`; otherwise returns `None`.
    - `or_(other)`: Returns the first `Some`, or the second `Option` if the first is `None`.
    - `and_then(func)`: Chains another operation based on the `Some` value.
    - `or_else(func)`: Chains another operation based on the `None` value.

## ⚙️ Usage Examples

Here are more practical examples of using `Result` and `Option` in real-world scenarios.

### Example: Handling API Responses

```python
from rusty_utils import Result, Ok, Err


def fetch_data() -> Result[dict, Exception]:
    try:
        # Simulating an API call
        data = {"id": 824, "name": "Kobe Bryant"}
        return Ok(data)
    except Exception as e:
        return Err(e)


result = fetch_data()

if result.is_ok():
    print("Success:", result.unwrap())
else:
    print("Error:", result.unwrap_err())
```

### Example: Safely Unwrapping Values

```python
from rusty_utils import Option


def get_value() -> Option[int]:
    return Option(42)


some_value = get_value()

print(some_value.unwrap_or(0))  # Outputs: 42
```

For more advanced use cases, consult the [full documentation](./docs/README.md).

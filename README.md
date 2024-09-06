# rusty-utils

Bringing useful tools from Rust to Python.

## :door: Portals

- [:door: Portals](#door-portals)
- [:inbox\_tray: Installation](#inbox_tray-installation)
- [:books: Features](#books-features)
  - [Result\[T, E\]](#resultt-e)
- [:gear: Usage Examples](#gear-usage-examples)
  - [Example: Handling API Responses](#example-handling-api-responses)
  - [Example: Safely Unwrapping Values](#example-safely-unwrapping-values)

## :inbox_tray: Installation

`rusty-utils` is available on [PyPI](https://pypi.org/project/rusty-utils/).

Install using `pip`:

```bash
pip install rusty-utils
```

Or with `poetry`:

```bash
poetry add rusty-utils
```

## :books: Features

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

#### Quickly wrap a function call

```python
import random

from rusty_utils import Catch, Result


# Let's assume this function may fail
def russian_roulette() -> str:
    if random.randint(0, 6) == 0:
        raise Exception("Bang!")
    else:
        return "Click!"


# Quickly wrap the function call in a Result
result: Result[str, Exception] = Catch(russian_roulette, Exception)
```
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
    - `map(func)`: Transforms the `Ok` value.
    - `map_err(func)`: Transforms the `Err` value.
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

## :gear: Usage Examples

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

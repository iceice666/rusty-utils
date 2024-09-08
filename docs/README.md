<!-- markdownlint-disable -->

# API Overview

## Modules

- [`common`](./common.md#module-common)
- [`option`](./option.md#module-option)
- [`result`](./result.md#module-result)

## Classes

- [`common.UnwrapError`](./common.md#class-unwraperror): Custom exception raised when an invalid 'unwrap' or 'unwrap_err' is called on a Result object.
- [`option.Option`](./option.md#class-option): A class that expands the built-in `Optional` type, representing a value that may or may not be present (`Some` or `None`).
- [`result.Result`](./result.md#class-result): A generic container that represents either success (`Ok` value) or failure (`Err` value).

## Functions

- [`result.Catch`](./result.md#function-catch): A decorator that returns a `Err` if captured an exception or `Ok` if the function returns successfully.
- [`result.Err`](./result.md#function-err): Creates a new `Result` object with the provided value as the `Err` value.
- [`result.Ok`](./result.md#function-ok): Creates a new `Result` object with the provided value as the `Ok` value.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

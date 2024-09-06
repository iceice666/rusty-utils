<!-- markdownlint-disable -->

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `result`





---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L314"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `Ok`

```python
Ok(value: ~T) → Result[T, E]
```

Creates a new `Result` object with the provided value as the `Ok` value. 



**Args:**
 
 - <b>`value`</b> (`T`):  The value to use as the `Ok` value. 



**Returns:**
 
 - <b>``Result[T, E]``</b>:  A new `Result` object with the provided value as the `Ok` value. 


---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L326"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `Err`

```python
Err(value: ~E) → Result[T, E]
```

Creates a new `Result` object with the provided value as the `Err` value. 



**Args:**
 
 - <b>`value`</b> (`E`):  The value to use as the `Err` value. 



**Returns:**
 
 - <b>``Result[T, E]``</b>:  A new `Result` object with the provided value as the `Err` value. 


---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L338"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `Catch`

```python
Catch(f: Callable[[], ~T], err_type: type[~E]) → Result[T, E]
```

Runs the provided function and returns a `Result` object with either the function's return value or the caught exception. 



**Args:**
 
 - <b>`f`</b> (`Callable[[], T]`):  The function to run. 
 - <b>`err_type`</b> (`type[E]`):  The type of exception to catch. 



**Returns:**
 
 - <b>``Result[T, E]``</b>:  A `Result` object with either the function's return value or the caught exception. 


---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Result`
A generic container that represents either success (`Ok` value) or failure (`Err` value). 



**Attributes:**
 
 - <b>`ok_value`</b> (`T`):  The value contained if the `Result` is successful. 
 - <b>`err_value`</b> (`E`):  The error contained if the `Result` is a failure. 
 - <b>`__is_ok__`</b> (`bool`):  A boolean indicating whether the `Result` is `Ok` (True) or `Err` (False). 

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(ok: Optional[~T] = None, err: Optional[~E] = None)
```

Initializes a `Result` object with either an `ok_value` or an `err_value`. 



**Args:**
 
 - <b>`ok`</b> (`Optional[T]`):  The value representing success. 
 - <b>`err`</b> (`Optional[E]`):  The value representing failure. 



**Raises:**
 
 - <b>``ValueError``</b>:  If both or neither `ok_value` and `err_value` are provided. 




---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L253"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `and_`

```python
and_(other: 'Result[U, E]') → Result[U, E]
```

Returns the provided `Result` if this `Result` is `Ok`, otherwise returns the current `Err`. 



**Args:**
 
 - <b>`other`</b> (`Result[U, E]`):  A `Result` object to return if this is an `Ok`. 



**Returns:**
 
 - <b>``Result[U, E]``</b>:  The provided `Result` or the current `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `and_then`

```python
and_then(f: Callable[[~T], ForwardRef('Result[U, E]')]) → Result[U, E]
```

Calls the provided function with the `Ok` value if this is an `Ok` `Result`. 



**Args:**
 
 - <b>`f`</b> (`Callable[[T], Result[U, E]]`):  A function to apply to the `Ok` value. 



**Returns:**
 
 - <b>``Result[U, E]``</b>:  A new `Result` produced by the function, or the current `Err` if this is an `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `err`

```python
err() → Option[E]
```

Retrieves the `Err` value if the `Result` is a failure. 



**Returns:**
 
 - <b>``Option[E]``</b>:  The `Err` value if present, otherwise `None`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect`

```python
expect(msg: str) → ~T
```

Unwraps the `Ok` value or raises an `UnwrapError` with the provided message if the `Result` is an `Err`. 



**Args:**
 
 - <b>`msg`</b> (str):  The error message to use if the `Result` is an `Err`. 



**Returns:**
 
 - <b>``T``</b>:  The `Ok` value if present. 



**Raises:**
 
 - <b>``UnwrapError``</b>:  If the `Result` is an `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L172"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect_err`

```python
expect_err(msg: str) → ~E
```

Unwraps the `Err` value or raises an `UnwrapError` with the provided message if the `Result` is an `Ok`. 



**Args:**
 
 - <b>`msg`</b> (str):  The error message to use if the `Result` is an `Ok`. 



**Returns:**
 
 - <b>``E``</b>:  The `Err` value if present. 



**Raises:**
 
 - <b>``UnwrapError``</b>:  If the `Result` is an `Ok`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `inspect`

```python
inspect(f: Callable[[~T], NoneType]) → Result[T, E]
```

Executes the provided function on the `Ok` value without transforming it. 



**Args:**
 
 - <b>`f`</b> (`Callable[[T], None]`):  A function to apply to the `Ok` value. 



**Returns:**
 
 - <b>``Result[T, E]``</b>:  The original `Result` object. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `inspect_err`

```python
inspect_err(f: Callable[[~E], NoneType]) → Result[T, E]
```

Executes the provided function on the `Err` value without transforming it. 



**Args:**
 
 - <b>`f`</b> (`Callable[[E], None]`):  A function to apply to the `Err` value. 



**Returns:**
 
 - <b>``Result[T, E]``</b>:  The original `Result` object. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_err`

```python
is_err() → bool
```

Checks if the `Result` is an `Err` value. 



**Returns:**
 
 - <b>``bool``</b>:  `True` if the `Result` is `Err`, otherwise `False`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_ok`

```python
is_ok() → bool
```

Checks if the `Result` is an `Ok` value. 



**Returns:**
 
 - <b>``bool``</b>:  `True` if the `Result` is `Ok`, otherwise `False`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map`

```python
map(f: Callable[[~T], ~U]) → Result[U, E]
```

Transforms the `Ok` value using the provided function. 



**Args:**
 
 - <b>`f`</b> (`Callable[[T], U]`):  A function to apply to the `Ok` value. 



**Returns:**
 
 - <b>``Result[U, E]``</b>:  A new `Result` with the transformed `Ok` value, or the original `Err` value if applicable. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_err`

```python
map_err(f: Callable[[~E], ~F]) → Result[T, F]
```

Transforms the `Err` value using the provided function. 



**Args:**
 
 - <b>`f`</b> (`Callable[[E], F]`):  A function to apply to the `Err` value. 



**Returns:**
 
 - <b>``Result[T, F]``</b>:  A new `Result` with the transformed `Err` value, or the original `Ok` value if applicable. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or`

```python
map_or(default: ~U, f: Callable[[~T], ~U]) → ~U
```

Transforms the `Ok` value or returns the default if the `Result` is an error. 



**Args:**
 
 - <b>`default`</b> (`U`):  The default value to return if the `Result` is an `Err`. 
 - <b>`f`</b> (`Callable[[T], U]`):  A function to apply to the `Ok` value. 



**Returns:**
 
 - <b>``U``</b>:  The transformed `Ok` value or the default value if the `Result` is an `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or_else`

```python
map_or_else(f_err: Callable[[~E], ~U], f_ok: Callable[[~T], ~U]) → ~U
```

Transforms the `Ok` or `Err` value using the provided functions based on the `Result`'s state. 



**Args:**
 
 - <b>`f_err`</b> (`Callable[[E], U]`):  A function to apply to the `Err` value. 
 - <b>`f_ok`</b> (`Callable[[T], U]`):  A function to apply to the `Ok` value. 



**Returns:**
 
 - <b>``U``</b>:  The result of applying `f_ok` to the `Ok` value or `f_err` to the `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ok`

```python
ok() → Option[T]
```

Retrieves the `Ok` value if the `Result` is successful. 



**Returns:**
 
 - <b>``Option[T]``</b>:  The `Ok` value if present, otherwise `None`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L275"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `or_`

```python
or_(other: 'Result[T, F]') → Result[T, F]
```

Returns the current `Ok` value or the provided `Result` if this is an `Err`. 



**Args:**
 
 - <b>`other`</b> (`Result[T, F]`):  A `Result` object to return if this is an `Err`. 



**Returns:**
 
 - <b>``Result[T, F]``</b>:  The current `Ok` value or the provided `Result`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L286"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `or_else`

```python
or_else(f: Callable[[~E], ForwardRef('Result[T, F]')]) → Result[T, F]
```

Calls the provided function with the `Err` value if this is an `Err` `Result`. 



**Args:**
 
 - <b>`f`</b> (`Callable[[E], Result[T, F]]`):  A function to apply to the `Err` value. 



**Returns:**
 
 - <b>``Result[T, F]``</b>:  A new `Result` produced by the function, or the current `Ok` value if this is an `Ok`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap`

```python
unwrap() → ~T
```

Unwraps the `Ok` value, or raises an `UnwrapError` if the `Result` is an `Err`. 



**Returns:**
 
 - <b>``T``</b>:  The `Ok` value if present. 



**Raises:**
 
 - <b>``UnwrapError``</b>:  If the `Result` is an `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L203"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_err`

```python
unwrap_err() → ~E
```

Unwraps the `Err` value, or raises an `UnwrapError` if the `Result` is an `Ok`. 



**Returns:**
 
 - <b>``E``</b>:  The `Err` value if present. 



**Raises:**
 
 - <b>``UnwrapError``</b>:  If the `Result` is an `Ok`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or`

```python
unwrap_or(default: ~T) → ~T
```

Returns the `Ok` value or a default value if the `Result` is an `Err`. 



**Args:**
 
 - <b>`default`</b> (`T`):  The value to return if the `Result` is an `Err`. 



**Returns:**
 
 - <b>``T``</b>:  The `Ok` value or the provided default value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L228"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_else`

```python
unwrap_or_else(f: Callable[[~E], ~T]) → ~T
```

Returns the `Ok` value or computes a default from the `Err` value using the provided function. 



**Args:**
 
 - <b>`f`</b> (`Callable[[E], T]`):  A function to compute a value from the `Err` value. 



**Returns:**
 
 - <b>``T``</b>:  The `Ok` value or the result of applying `f` to the `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_raise`

```python
unwrap_or_raise() → ~T
```

Unwraps the `Ok` value, or raises the `Err` value if it is an exception. 



**Returns:**
 
 - <b>``T``</b>:  The `Ok` value if present. 



**Raises:**
 The `Err` value if it is an exception. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

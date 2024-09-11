<!-- markdownlint-disable -->

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `result`




**Global Variables**
---------------
- **TYPE_CHECKING**

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L276"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `Catch`

```python
Catch(
    *err_type: type[~E],
    func: Optional[Callable[~P, ~T]] = None
) → Union[Callable[[Callable[~P, ~T]], Callable[~P, ForwardRef('Result[T, E]')]], ForwardRef('Result[T, E]')]
```

A decorator that captures exceptions and returns a `Result`. 

If an exception occurs, it returns an `Err` containing the exception;  otherwise, it returns an `Ok` containing the function's result. 



**Args:**
 
 - <b>`err_type`</b> (type[E]):  One or more exception types to catch. 
 - <b>`func`</b> (Callable[P, T]):  The function to execute. 



**Returns:**
 Either a `Result` containing `Ok` if the function executes without exception, or an `Err`. 


---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Ok`
Represents a successful `Result` with an `Ok` value. 



**Attributes:**
 
 - <b>`value`</b> (T):  The value held in a successful `Result`. 

<a href="https://github.com/iceice666/rusty-utils/blob/main/<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(value: ~T) → None
```








---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `and_`

```python
and_(other: 'Result[U, E]') → Result[U, E]
```

Returns the provided `Result` if this `Result` is `Ok`, otherwise returns the current `Err`. 



**Args:**
 
 - <b>`other`</b> (Result[U, E]):  A `Result` object to return if this is an `Ok`. 



**Returns:**
 
 - <b>`Result[U, E]`</b>:  The provided `Result` or the current `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `err`

```python
err() → Option[E]
```

Retrieves the `Err` value, which in this case is `None` since it's an `Ok`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect`

```python
expect(msg: str) → ~T
```

Unwraps the `Ok` value or raises an `UnwrapError` with the provided message if the result is an `Err`. 



**Args:**
 
 - <b>`msg`</b> (str):  Error message for an `Err` result. 



**Returns:**
 
 - <b>`T`</b>:  The `Ok` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect_err`

```python
expect_err(msg: str) → ~E
```

Raises an `UnwrapError` because this is an `Ok` value. 



**Args:**
 
 - <b>`msg`</b> (str):  The error message. 



**Raises:**
 
 - <b>`UnwrapError`</b>:  Always raises an error because this is an `Ok`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_err`

```python
is_err() → bool
```

Checks if the `Result` is an `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_ok`

```python
is_ok() → bool
```

Checks if the `Result` is an `Ok` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map`

```python
map(f: Callable[[~T], ~U]) → Result[U, E]
```

Transforms the `Ok` value using the provided function. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_err`

```python
map_err(f: Callable[[~E], ~F]) → Result[T, F]
```

Passes through the `Ok` value without transforming the `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or`

```python
map_or(default: ~U, f: Callable[[~T], ~U]) → ~U
```

Transforms the `Ok` value using the function or returns a default if `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or_else`

```python
map_or_else(f_err: Callable[[~E], ~U], f_ok: Callable[[~T], ~U]) → ~U
```

Transforms the `Ok` value using the provided function. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ok`

```python
ok() → Option[T]
```

Retrieves the `Ok` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `or_`

```python
or_(other: 'Result[T, F]') → Result[T, F]
```

Returns the current `Ok` value or the provided `Result` if this is an `Err`. 



**Args:**
 
 - <b>`other`</b> (Result[T, F]):  A `Result` object to return if this is an `Err`. 



**Returns:**
 
 - <b>`Result[T, F]`</b>:  The current `Ok` value or the provided `Result`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap`

```python
unwrap() → ~T
```

Unwraps the `Ok` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_err`

```python
unwrap_err() → ~E
```

Raises an `UnwrapError` because this is an `Ok` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or`

```python
unwrap_or(default: ~T) → ~T
```

Returns the `Ok` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_else`

```python
unwrap_or_else(f: Callable[[~E], ~T]) → ~T
```

Returns the `Ok` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_raise`

```python
unwrap_or_raise() → ~T
```

Unwraps the `Ok` value. 


---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Err`
Represents a failed `Result` with an `Err` value. 



**Attributes:**
 
 - <b>`value`</b> (E):  The error contained in the `Err`. 

<a href="https://github.com/iceice666/rusty-utils/blob/main/<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(value: ~E) → None
```








---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L229"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `and_`

```python
and_(other: 'Result[U, E]') → Result[U, E]
```

Returns the provided `Result` if this `Result` is `Ok`, otherwise returns the current `Err`. 



**Args:**
 
 - <b>`other`</b> (Result[U, E]):  A `Result` object to return if this is an `Ok`. 



**Returns:**
 
 - <b>`Result[U, E]`</b>:  The provided `Result` or the current `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `err`

```python
err() → Option[E]
```

Retrieves the `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect`

```python
expect(msg: str) → ~T
```

Raises an `UnwrapError` with the provided message because this is an `Err`. 



**Args:**
 
 - <b>`msg`</b> (str):  Error message for unwrapping. 



**Raises:**
 
 - <b>`UnwrapError`</b>:  Always raises an error since this is an `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L197"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect_err`

```python
expect_err(msg: str) → ~E
```

Unwraps the `Err` value or raises an `UnwrapError` with the provided message if the result is an `Ok`. 



**Args:**
 
 - <b>`msg`</b> (str):  Error message for unwrapping an `Ok` value. 



**Returns:**
 
 - <b>`E`</b>:  The `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_err`

```python
is_err() → bool
```

Checks if the `Result` is an `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_ok`

```python
is_ok() → bool
```

Checks if the `Result` is an `Ok` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L169"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map`

```python
map(f: Callable[[~T], ~U]) → Result[U, E]
```

Passes through the `Err` value without transforming it. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_err`

```python
map_err(f: Callable[[~E], ~F]) → Result[T, F]
```

Transforms the `Err` value using the provided function. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L173"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or`

```python
map_or(default: ~U, f: Callable[[~T], ~U]) → ~U
```

Returns the default value as this is an `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L177"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or_else`

```python
map_or_else(f_err: Callable[[~E], ~U], f_ok: Callable[[~T], ~U]) → ~U
```

Transforms the `Err` value using the provided function. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L159"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ok`

```python
ok() → Option[T]
```

Retrieves the `Ok` value, which is `None` in this case. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L241"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `or_`

```python
or_(other: 'Result[T, F]') → Result[T, F]
```

Returns the current `Ok` value or the provided `Result` if this is an `Err`. 



**Args:**
 
 - <b>`other`</b> (Result[T, F]):  A `Result` object to return if this is an `Err`. 



**Returns:**
 
 - <b>`Result[T, F]`</b>:  The provided `Result` or the current `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap`

```python
unwrap() → ~T
```

Raises an `UnwrapError` because this is an `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_err`

```python
unwrap_err() → ~E
```

Unwraps the `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or`

```python
unwrap_or(default: ~T) → ~T
```

Returns the default value since this is an `Err`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_else`

```python
unwrap_or_else(f: Callable[[~E], ~T]) → ~T
```

Computes a default from the `Err` value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\result.py#L225"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_raise`

```python
unwrap_or_raise() → ~T
```

Raises the `Err` value since this is an error. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

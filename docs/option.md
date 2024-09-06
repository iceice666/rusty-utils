<!-- markdownlint-disable -->

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `option`






---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Option`
A class that expands the built-in `Optional` type, representing a value that may or may not be present (`Some` or `None`). 



**Attributes:**
 
 - <b>`value`</b> (`T | None`):  The value stored in the `Option` or `None` if no value is present. 

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(value: Optional[~T] = None)
```

Initialize the `Option` class with an optional value. 



**Args:**
 
 - <b>`value`</b> (`T | None`):  The value to be stored in the `Option`, or `None` if absent. 




---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L188"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `and_`

```python
and_(optb: 'Option[U]') → Option[U]
```

Return the second `Option` if the first is `Some`, otherwise return `None`. 



**Args:**
 
 - <b>`optb`</b> (`Option[U]`):  The second `Option` to return if the first is `Some`. 



**Returns:**
 
 - <b>``Option[U]``</b>:  The second `Option` if the first is `Some`, otherwise `None`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `and_then`

```python
and_then(f: Callable[[~T], ForwardRef('Option[U]')]) → Option[U]
```

Call a function if the `Option` is `Some` and return its result, otherwise return `None`. 



**Args:**
 
 - <b>`f`</b> (`Callable[[T], Option[U]]`):  A function that takes the contained value and returns a new `Option`. 



**Returns:**
 
 - <b>``Option[U]``</b>:  The result of the function if `Some`, otherwise `None`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect`

```python
expect(message: str) → ~T
```

Return the contained value or raise a `ValueError` with the provided message if `None`. 



**Args:**
 
 - <b>`message`</b> (str):  The message for the error if the `Option` contains no value. 



**Returns:**
 
 - <b>``T``</b>:  The contained value. 



**Raises:**
 
 - <b>``ValueError``</b>:  If the `Option` contains no value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `inspect`

```python
inspect(f: Callable[[~T], NoneType]) → Option[T]
```

Call a function with the contained value for side effects and return the `Option` unchanged. 



**Args:**
 
 - <b>`f`</b> (`Callable[[T], None]`):  A function that takes the contained value for side effects. 



**Returns:**
 
 - <b>``Option[T]``</b>:  The original `Option`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_none`

```python
is_none() → bool
```

Check if the `Option` contains no value. 



**Returns:**
 
 - <b>`bool`</b>:  `True` if the `Option` contains no value, `False` otherwise. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_some`

```python
is_some() → bool
```

Check if the `Option` contains a value. 



**Returns:**
 
 - <b>`bool`</b>:  `True` if the `Option` contains a value, `False` otherwise. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_some_and`

```python
is_some_and(f: Callable[[~T], bool]) → bool
```

Check if the `Option` contains a value and the predicate returns `True`. 



**Args:**
 
 - <b>`f`</b> (`Callable[[T], bool]`):  A function that takes the value and returns a `bool`. 



**Returns:**
 
 - <b>`bool`</b>:  `True` if the `Option` contains a value and the predicate is `True`, `False` otherwise. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map`

```python
map(f: Callable[[~T], ~U]) → Option[U]
```

Apply a function to the contained value and return a new `Option` containing the result. 



**Args:**
 
 - <b>`f`</b> (`Callable[[T], U]`):  A function that takes the contained value and returns a new value. 



**Returns:**
 
 - <b>``Option[U]``</b>:  A new `Option` with the result of the function or `None` if the original `Option` was `None`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or`

```python
map_or(default: ~U, f: Callable[[~T], ~U]) → ~U
```

Apply a function to the contained value or return the provided default if `None`. 



**Args:**
 
 - <b>`default`</b> (`U`):  The default value to return if the `Option` contains no value. 
 - <b>`f`</b> (`Callable[[T], U]`):  A function that takes the contained value and returns a new value. 



**Returns:**
 
 - <b>``U``</b>:  The result of the function or the default value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or_else`

```python
map_or_else(default_f: Callable[[], ~U], f: Callable[[~T], ~U]) → ~U
```

Apply a function to the contained value or return the result of a default function if `None`. 



**Args:**
 
 - <b>`default_f`</b> (`Callable[[], U]`):  A function that returns a default value if the `Option` contains no value. 
 - <b>`f`</b> (`Callable[[T], U]`):  A function that takes the contained value and returns a new value. 



**Returns:**
 
 - <b>``U``</b>:  The result of the function or the result of the default function. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ok_or`

```python
ok_or(err: ~E) → Result[T, E]
```

Convert the `Option` to a `Result`, returning `Ok(value)` if `Some`, or `Err(err)` if `None`. 



**Args:**
 
 - <b>`err`</b> (`E`):  The error to return if the `Option` contains no value. 



**Returns:**
 
 - <b>``Result[T, E]``</b>:  `Ok` with the value if `Some`, `Err` with the error if `None`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ok_or_else`

```python
ok_or_else(err_f: Callable[[], ~E]) → Result[T, E]
```

Convert the `Option` to a `Result`, returning `Ok(value)` if `Some`, or `Err` from a function if `None`. 



**Args:**
 
 - <b>`err_f`</b> (`Callable[[], E]`):  A function that returns an error if the `Option` contains no value. 



**Returns:**
 
 - <b>``Result[T, E]``</b>:  `Ok` with the value if `Some`, `Err` with the result of the function if `None`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L210"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `or_`

```python
or_(optb: 'Option[T]') → Option[T]
```

Return the first `Option` if it's `Some`, otherwise return the second `Option`. 



**Args:**
 
 - <b>`optb`</b> (`Option[T]`):  The second `Option` to return if the first is `None`. 



**Returns:**
 
 - <b>``Option[T]``</b>:  The first `Option` if it's `Some`, otherwise the second `Option`. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `or_else`

```python
or_else(f: Callable[[], ForwardRef('Option[T]')]) → Option[T]
```

Return the first `Option` if it's `Some`, otherwise return the result of a function. 



**Args:**
 
 - <b>`f`</b> (`Callable[[], Option[T]]`):  A function that returns a new `Option` if the first is `None`. 



**Returns:**
 
 - <b>``Option[T]``</b>:  The first `Option` if it's `Some`, otherwise the result of the function. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap`

```python
unwrap() → ~T
```

Return the contained value or raise an `UnwrapError` if `None`. 



**Returns:**
 
 - <b>``T``</b>:  The contained value. 



**Raises:**
 
 - <b>``UnwrapError``</b>:  If the `Option` contains no value. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or`

```python
unwrap_or(default: ~T) → ~T
```

Return the contained value or the provided default if `None`. 



**Args:**
 
 - <b>`default`</b> (`T`):  The default value to return if the `Option` contains no value. 



**Returns:**
 
 - <b>``T``</b>:  The contained value or the default. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_else`

```python
unwrap_or_else(f: Callable[[], ~T]) → ~T
```

Return the contained value or the result of the provided function if `None`. 



**Args:**
 
 - <b>`f`</b> (`Callable[[], T]`):  A function that returns a value to be used if the `Option` contains no value. 



**Returns:**
 
 - <b>``T``</b>:  The contained value or the result of the function. 

---

<a href="https://github.com/iceice666/rusty-utils/blob/main/rusty_utils\option.py#L232"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `xor`

```python
xor(optb: 'Option[T]') → Option[T]
```

Return `Some` if exactly one of the options is `Some`, otherwise return `None`. 



**Args:**
 
 - <b>`optb`</b> (`Option[T]`):  The other `Option` to compare with. 



**Returns:**
 
 - <b>``Option[T]``</b>:  `Some` if exactly one of the options is `Some`, otherwise `None`. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

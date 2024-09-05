from typing import TypeVar, Generic
from abc import abstractmethod

class UnwrapError(Exception):
    def __init__(self, msg): super().__init__(msg)
    

_T = TypeVar("_T")
_U = TypeVar("_U")
_E = TypeVar("_E", bound=Exception)
Result = Union['Ok[_T]', 'Err[_E]']


class Ok(Generic[_T]):
    data: _T
    def __init__(self, data: _T):
        self.data = data
        
    def is_ok(self) -> bool: return True
    def is_err(self) -> bool: return False
    def expect(self) -> _T: self.data
    def expect_err(self) :
        raise UnwrapError(f"called `Result.expect_err` on an `Ok` value: {self}")
    def unwrap(self) -> _T: self.data
    def unwrap_err(self) :
        raise UnwrapError(f"called `Result.unwrap_err` on an `Ok` value: {self}")
    def unwrap_or(self, default: _T) -> _T: self.data
    def unwrap_or_else(self, f: Callable[[_E], _T]) -> _T: self.data
    def map(self, f: Callable[[_T], _U]) -> Result[_U, _E]:
        self.data = f(self.data)
        return self
    def map_err(self, f: Callable[[_E], _U]) -> Result[_T, _U]: return self
    def map_or(self, default: _U, f: Callable[[_T], _U]) -> _U: return f(self.data)
    def map_or_else(self, default_f: Callable[[_E], _U], f: Callable[[_T], _U]) -> _U: return f(self.data)
    def ok(self) -> _T: return self.data
    def err(self) -> None: return None
    
class Err(Generic[_E]):
    err: _E
    def __init__(self, err:_E):
        self.err = err
        
    def is_ok(self) -> bool: return False
    def is_err(self) -> bool: return True
    def expect(self) :
        raise UnwrapError(f"called `Result.expect` on an `Err` value: {self}")
    def expect_err(self) -> _E: self.err
    def unwrap(self) -> _T:
        raise UnwrapError(f"called `Result.unwrap` on an `Err` value: {self}")
    def unwrap_err(self) -> _E: self.err
    def unwrap_or(self, default: _T) -> _T: return default
    def unwrap_or_else(self, f: Callable[[_E], _T]) -> _T: return f(self.err)
    def map(self, f: Callable[[_T], _U]) -> Result[_U, _E]: return self
    def map_err(self, f: Callable[[_E], _U]) -> Result[_T, _U]:
        self.err = f(self.err)
        return self
    def map_or(self, default: _U, f: Callable[[_T], _U]) -> _U: return default
    def map_or_else(self, default_f: Callable[[_E], _U], f: Callable[[_T], _U]) -> _U: return default_f(self.err)
    def ok(self) -> None: return None
    def err(self) -> _E : return self.err



from abc import abstractmethod
from typing import Protocol, TypeVar

class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: CT, other: CT) -> bool: ...

class Addable(Protocol):
    @abstractmethod
    def __add__(self: AT, other: AT) -> AT: ...
CT = TypeVar('CT', bound=Comparable)
AT = TypeVar('AT', bound=Addable)

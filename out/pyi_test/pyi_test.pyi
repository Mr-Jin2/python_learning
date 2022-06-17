from _typeshed import Incomplete

class Student:
    name: Incomplete
    id: Incomplete
    def __init__(self, name: str, id: str) -> None: ...
    @property
    def score(self) -> int: ...
    @score.setter
    def score(self, value: int): ...

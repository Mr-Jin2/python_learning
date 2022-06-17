class Student:

    def __init__(self,
                 name: str,
                 id: str):
        self.name = name
        self.id = id

    @property
    def score(self) -> int:
        return self.score

    @score.setter
    def score(self, value: int):
        self.score = value
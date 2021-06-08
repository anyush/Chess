from abc import ABC, abstractmethod
from enum import Enum


class FigureColor(Enum):
    white = 0
    black = 1

    def __str__(self):
        return "white" if self == FigureColor.white else "black"


class Figure(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name}_{self.color}"

    @abstractmethod
    def find_possible_moves(self, desk, x, y):
        pass

    def move(self, cell_from, cell_to):
        cell_from.figure = None
        cell_to.figure = self


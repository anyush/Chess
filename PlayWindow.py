from PyQt5.QtWidgets import QWidget
from Cell import *
from Figure import FigureColor
from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook


class PlayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.desk = [[Cell(None, None, 0, 0, None) for i in range(8)] for j in range(8)]
        self.selected_cell = None
        self.last_color = FigureColor.black

        self.init_desk()

    def init_desk(self):
        dsk = [[4, 6, 8, 10, 12, 8, 6, 4],
               [2, 2, 2, 2, 2, 2, 2, 2],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [3, 5, 7, 9, 11, 7, 5, 3]]

        white = FigureColor.white
        black = FigureColor.black

        figures = [None, (Pawn, white), (Pawn, black), (Rook, white), (Rook, black), (Knight, white), (Knight, black),
                   (Bishop, white), (Bishop, black), (Queen, white), (Queen, black), (King, white), (King, black)]

        cell_color = CellColor.dark
        y_pos = 100
        for y, line in enumerate(dsk):
            x_pos = 100
            cell_color = CellColor.bright if cell_color == CellColor.dark else CellColor.dark
            for x, fig_id in enumerate(line):
                figure = None if figures[fig_id] is None else figures[fig_id][0](figures[fig_id][1])
                self.desk[y][x] = Cell(self, self.desk, x, y, cell_color, figure=figure)
                self.desk[y][x].show()
                self.desk[y][x].setGeometry(x_pos, y_pos, 50, 50)
                if figure is not None and figure.color == FigureColor.white:
                    self.desk[y][x].activate()
                else:
                    self.desk[y][x].deactivate()
                x_pos += 50
            y_pos += 50

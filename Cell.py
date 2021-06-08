from enum import Enum
from Figure import FigureColor
from PyQt5.QtWidgets import QPushButton


class CellColor(Enum):
    bright = 0
    dark = 1

    def __str__(self):
        return "bright" if self == CellColor.bright else "dark"


GRAPHICS_DIR = "./Graphics/"


class Cell(QPushButton):
    def __repr__(self):
        return self.name + ' ' + str(self.x) + ' ' + str(self.y)

    def __init__(self, parent, desk, x, y, color, *argc, figure=None, background_img='.png'):
        super().__init__(parent)
        self.parent = parent
        self.desk = desk
        self.figure = figure
        self.color = color
        self.x = x
        self.y = y
        self.background_img = background_img
        self.active = False
        self.clicked.connect(self.click)

    def get_texture_head(self):
        return GRAPHICS_DIR + f"{'empty' if self.figure is None else str(self.figure)}"

    def set_texture(self, texture):
        self.setStyleSheet(f"background-image: url('{texture}'); border: none")

    def enterEvent(self, event):
        if not self.active:
            return

        if self.parent.selected_cell is self or self.figure is None or self.figure.color != self.parent.last_color:
            background_img = self.get_texture_head() + "_active_covered.png"
        else:
            background_img = self.get_texture_head() + "_attacked_covered.png"

        self.set_texture(background_img)

    def leaveEvent(self, event):
        if not self.active:
            return

        if self.parent.selected_cell is self or self.figure is None or self.figure.color != self.parent.last_color:
            background_img = self.get_texture_head() + "_active.png"
        else:
            background_img = self.get_texture_head() + "_attacked.png"

        self.set_texture(background_img)

    def activate(self):
        self.active = True
        if self.figure is None or self.figure.color != self.parent.last_color:
            background_img = self.get_texture_head() + "_active.png"
        else:
            background_img = self.get_texture_head() + "_attacked.png"
        self.set_texture(background_img)

    def deactivate(self):
        self.active = False
        background_img = self.get_texture_head() + "_" + str(self.color) + ".png"
        self.set_texture(background_img)

    def click(self):
        if not self.active:
            return

        if self.parent.selected_cell is None:
            self.parent.selected_cell = self
            cell_data = self.figure.find_possible_moves(self.desk, self.x, self.y)
            for y in range(8):
                for x in range(8):
                    self.desk[y][x].deactivate()
            self.activate()
            for cell in cell_data[0]:
                cell.activate()
            for cell in cell_data[1]:
                cell.activate()

        elif self.parent.selected_cell is self:
            for y in range(8):
                for x in range(8):
                    if self.desk[y][x].figure is not None and \
                            self.desk[y][x].figure.color != self.parent.last_color:
                        self.desk[y][x].activate()
                    else:
                        self.desk[y][x].deactivate()
            self.parent.selected_cell = None
        else:
            self.parent.selected_cell.figure.move(self.parent.selected_cell, self)
            self.parent.selected_cell = None
            self.parent.last_color = FigureColor.white if self.parent.last_color == FigureColor.black else \
                FigureColor.black
            for y in range(8):
                for x in range(8):
                    if self.desk[y][x].figure is not None and \
                            self.desk[y][x].figure.color != self.parent.last_color:
                        self.desk[y][x].activate()
                    else:
                        self.desk[y][x].deactivate()


        # if self.parent.selected_cell is None and self.figure is not None and self.color != self.paren.last_color:
        #     self.active = True
        #     self.parent.selected_cell = self
        #     cell_data = self.figure.find_possible_moves()
        #
        #
        #
        #
        # elif last_clicked_button is self and (
        #         ('king' in self.name and self in checkmate_cells(self.color)) is False or self.sender() is not self):
        #     self.active = False
        #     last_clicked_button = None
        #     for cell in (cell_data[0] + cell_data[1]):
        #         if (cell.x + cell.y) % 2 == 0:
        #             cell_color = 'bright'
        #         else:
        #             cell_color = 'dark'
        #         cell.setStyleSheet(
        #             "background-image: url('./Graphics/{}_{}.png'); border: none".format(cell.name, cell_color))
        #         cell.active = False
        # elif self.active and (
        #         ('king' in self.name and self in checkmate_cells(self.color)) is False or self.sender() is not self):
        #     button = last_clicked_button
        #     last_clicked_button.click()
        #     last_color *= -1
        #
        #     self.name = button.name
        #     self.color = button.color
        #     if (self.x + self.y) % 2 == 0:
        #         cell_color = '_bright'
        #     else:
        #         cell_color = '_dark'
        #     self.background_img = './Graphics/' + self.name + cell_color + '.png'
        #     self.setStyleSheet("background-image: url({}); border: none".format(self.background_img))
        #
        #     button.name = 'empty'
        #     button.color = 0
        #     if (button.x + button.y) % 2 == 0:
        #         cell_color = '_bright'
        #     else:
        #         cell_color = '_dark'
        #     button.background_img = './Graphics/empty' + cell_color + '.png'
        #     button.setStyleSheet("background-image: url({}); border: none".format(button.background_img))
        #
        #     if 'king' in self.name and abs(self.x - button.x) > 1:
        #         if self.x == 1:
        #             desk[self.y][2].name = desk[self.y][0].name
        #             desk[self.y][2].color = desk[self.y][0].color
        #             desk[self.y][0].name = 'empty'
        #             desk[self.y][0].color = 0
        #             if self.y % 2 == 0:
        #                 cell_color = '_bright'
        #             else:
        #                 cell_color = '_dark'
        #             desk[self.y][0].setStyleSheet(
        #                 "background-image: url('./Graphics/empty{}.png'); border: none".format(cell_color))
        #             desk[self.y][2].setStyleSheet("background-image: url('./Graphics/{}.png'); border: none".format(
        #                 desk[self.y][2].name + cell_color))
        #
        #     global white_castling_left
        #     global white_castling_right
        #     global black_castling_left
        #     global black_castling_right
        #
        #     if 'king' in self.name:
        #         if self.color == 1:
        #             white_castling_left = True
        #             white_castling_right = True
        #             global white_king_x
        #             global white_king_y
        #             white_king_x = self.x
        #             white_king_y = self.y
        #         else:
        #             black_castling_left = True
        #             black_castling_right = True
        #             global black_king_x
        #             global black_king_y
        #             black_king_x = self.x
        #             black_king_y = self.y
        #     elif 'rook' in self.name:
        #         if button.x == 0:
        #             if self.color == 1:
        #                 white_castling_left = True
        #             else:
        #                 black_castling_left = True
        #         elif button.x == 7:
        #             if self.color == 1:
        #                 white_castling_right = True
        #             else:
        #                 black_castling_right = True
        #     elif 'pawn' in self.name:
        #         if abs(button.y - self.y) == 2 and desk[button.y - self.color][button.x] in checkmate_cells(self.color,
        #                                                                                                     only_pawns=True):
        #             self.name = button.name
        #             self.color = button.color
        #             if (self.x + self.y) % 2 == 0:
        #                 cell_color = '_bright'
        #             else:
        #                 cell_color = '_dark'
        #             self.background_img = './Graphics/' + self.name + cell_color + '.png'
        #             self.setStyleSheet("background-image: url({}); border: none".format(self.background_img))
        #     Cell_data.king(white_king_y, white_king_x, 1)
        #     Cell_data.king(black_king_y, black_king_x, -1)
        #     if last_color == -1 and desk[white_king_y][white_king_x] in checkmate_cells(1):
        #         desk[white_king_y][white_king_x].click()
        #         desk[white_king_y][white_king_x].setStyleSheet(
        #             "background-image: url('./Graphics/king_white_active.png'); border: none")
        #     elif last_color == 1 and desk[black_king_y][black_king_x] in checkmate_cells(-1):
        #         desk[black_king_y][black_king_x].click()
        #         desk[black_king_y][black_king_x].setStyleSheet(
        #             "background-image: url('./Graphics/king_black_active.png'); border: none")

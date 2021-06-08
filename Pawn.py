from Figure import *


class Pawn(Figure):
    def __init__(self, color):
        super().__init__("pawn", color)
        self.moved_already = False

    def find_possible_moves(self, desk, x, y):
        move = []
        attack = []

        direction = 1 if self.color == FigureColor.white else -1

        if y > 0:
            if desk[y-direction][x].figure is None:
                move.append(desk[y-direction][x])
                if not self.moved_already and desk[y-2*direction][x].figure is None:
                    move.append(desk[y-2*direction][x])

            if x > 0 and desk[y-direction][x-1].figure is not None and \
                    desk[y-direction][x-1].figure.color != self.color:
                attack.append(desk[y-direction][x-1])
            if x < 7 and desk[y-direction][x+1].figure is not None and \
                    desk[y-direction][x+1].figure.color != self.color:
                attack.append(desk[y-direction][x+1])

        return move, attack

    def move(self, cell_from, cell_to):
        super().move(cell_from, cell_to)
        self.moved_already = True

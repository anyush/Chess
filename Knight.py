from Figure import *


class Knight(Figure):
    def __init__(self, color):
        super().__init__("knight", color)

    def find_possible_moves(self, desk, x, y):
        positions = ((x-1, y-2),
                     (x+1, y-2),
                     (x-2, y-1),
                     (x-2, y+1),
                     (x+2, y-1),
                     (x+2, y+1),
                     (x-1, y+2),
                     (x+1, y+2))

        move = []
        attack = []

        for pos in positions:
            x, y = pos

            if -1 < x < 8 and -1 < y < 8:
                if desk[y][x].figure is None:
                    move.append(desk[y][x])
                elif desk[y][x].figure.color != self.color:
                    attack.append(desk[y][x])

        return move, attack

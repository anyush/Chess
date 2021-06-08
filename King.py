from Figure import *


class King(Figure):
    def __init__(self, color):
        super().__init__("king", color)

    def find_possible_moves(self, desk, x, y):
        positions = tuple((px, py) for px in range(x-1, x+2) for py in range(y-1, y+2)
                          if (px != x or py != y) and -1 < px < 8 and -1 < py < 8)
        move = []
        attack = []

        for pos in positions:
            x, y = pos

            if desk[y][x].figure is None:
                move.append(desk[y][x])
            elif desk[y][x].figure.color != self.color:
                attack.append(desk[y][x])

        return move, attack

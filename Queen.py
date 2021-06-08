from Figure import *


class Queen(Figure):
    def __init__(self, color):
        super().__init__("queen", color)

    def find_possible_moves(self, desk, x, y):
        move = []
        attack = []

        all_positions = tuple(zip(range(x - 1, -1, -1), range(y - 1, -1, -1))), \
            tuple(zip(range(x + 1, 8), range(y - 1, -1, -1))), \
            tuple(zip(range(x - 1, -1, -1), range(y + 1, 8))), \
            tuple(zip(range(x + 1, 8), range(y + 1, 8))), \
            tuple(zip(range(x - 1, -1, -1), (y for i in range(7)))), \
            tuple(zip(range(x + 1, 8), (y for i in range(7)))), \
            tuple(zip((x for i in range(7)), range(y - 1, -1, -1))), \
            tuple(zip((x for i in range(7)), range(y + 1, 8)))

        for positions in all_positions:
            for pos in positions:
                x, y = pos
                if desk[y][x].figure is None:
                    move.append(desk[y][x])
                elif desk[y][x].figure.color != self.color:
                    attack.append(desk[y][x])
                    break
                else:
                    break

        return move, attack

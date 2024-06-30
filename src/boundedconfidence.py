import random

class Cell:
    """ Each cell in the population grid """
    def __init__(self, op, pos, grid_size):
        self.op = op
        self.posx = pos[0]
        self.posy = pos[1]
        self.grid_size = grid_size

    def getNeighbors(self):
        row, col = self.posx, self.posy
        shifts = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in shifts:
            nr = (row + dr) % self.grid_size
            nc = (col + dc) % self.grid_size
            neighbors.append((nr, nc))
        return neighbors

c1 = Cell(0.5, [0, 10], 100)
print(c1.getNeighbors())
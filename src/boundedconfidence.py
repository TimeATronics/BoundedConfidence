import random
import matplotlib.pyplot as plt
import numpy as np

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

grid_size = 30
learning_rate = 0.25
confidence_threshold = 0.5

tolerance = 0.05
grid = {}
for row in range(grid_size):
    for col in range(grid_size):
        grid[(row, col)] = Cell(round(random.uniform(0, 1), 2), [row, col], grid_size)

#for i, j in list(grid.items()):
#    print(i, ": ", j.op)

vis = [[0 for x in range(grid_size)] for y in range(grid_size)]
for row in range(len(vis)):
    for col in range(len(vis[0])):
        vis[row][col] = grid.get((row, col)).op
plt.clf()
plt.imshow(vis, origin='lower')
plt.show()

time_steps = 10000
for t in range(time_steps):
    pos1, cell1 = random.choice(list(grid.items()))
    neighbors = cell1.getNeighbors()
    '''
    # Non-spatial:
    pos2, cell2 = random.choice(list(grid.items()))
    if pos2 == pos1:
        while(pos1 == pos2):
            pos2, cell2 = random.choice(list(grid.items()))
    '''
    # Spatial:
    pos2 = random.choice(neighbors)
    cell2 = grid[pos2]
    #print("t = ", t)
    #print((cell1.posx, cell1.posy), ": ", cell1.op, (cell2.posx, cell2.posy), ": ", cell2.op)
    x1 = cell1.op
    x2 = cell2.op
    if (abs(x1 - x2) < confidence_threshold - tolerance * 2):
        x1_new = x1 + learning_rate * (x2 - x1)
        x2_new = x2 + learning_rate * (x1 - x2)
        cell1.op = round(x1_new, 2)
        cell2.op = round(x2_new, 2)
    # Negative Influence:
    elif (abs(x1 - x2) > confidence_threshold + tolerance * 2):
        if (x1 > x2):
            x1_new = (x1 + learning_rate * (x1 - x2) * (1 - x1))
            x2_new = (x2 + learning_rate * (x2 - x1) * x2)
            cell1.op = round(x1_new, 2)
            cell2.op = round(x2_new, 2)
        else:
            x1_new = (x1 + learning_rate * (x1 - x2) * x1)
            x2_new = (x2 + learning_rate * (x2 - x1) * (1 - x2))
            cell1.op = round(x1_new, 2)
            cell2.op = round(x2_new, 2)
    #print((cell1.posx, cell1.posy), ": ", cell1.op, (cell2.posx, cell2.posy), ": ", cell2.op)
    #print()

# Todo: familiar cells
# Visualization
for row in range(len(vis)):
    for col in range(len(vis[0])):
        vis[row][col] = grid.get((row, col)).op
plt.clf()
plt.imshow(vis, origin='lower')
plt.show()
class Cell:
    xlimit = 99
    ylimit = 99
    def __init__(self, op, pos):
        self.op = 0
        self.posx = 0
        self.posy = 0
    def get_neighbors(self):
        if (self.posx != 99) and (self.posy != 99):
            return [[self.posx + 1, self.posy], [self.posx, self.posy + 1], [self.posx - 1, self.posy], [self.posx, self.posy - 1]]
        elif (self.posx == 99) and (self.posy != 99):
            return [[self.posx + 1, self.posy], [self.posx, self.posy + 1], [self.posx - 1, self.posy], [self.posx, self.posy - 1]]
        elif (self.posx != 99) and (self.posy == 99):
            return [[self.posx + 1, self.posy], [self.posx, self.posy + 1], [self.posx - 1, self.posy], [self.posx, self.posy - 1]]
        elif (self.posx == 99) and (self.posy == 99):
            return [[self.posx + 1, self.posy], [self.posx, self.posy + 1], [self.posx - 1, self.posy], [self.posx, self.posy - 1]]

class Population:
    def __init__(self, size):
        size = 100
    def chooseRandomCell(self):
        return 1

def main():
    pop_size = 100

if __name__ == "__main__":
    main()
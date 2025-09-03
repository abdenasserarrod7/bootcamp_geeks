# ------ Exercise 1

import time
import copy

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        # Initialize grid: 0 = dead, 1 = alive
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        if initial_state:
            for (r, c) in initial_state:
                if 0 <= r < rows and 0 <= c < cols:
                    self.grid[r][c] = 1

    def display(self):
        for row in self.grid:
            print(" ".join('█' if cell else ' ' for cell in row))
        print("\n" + "-"*self.cols*2 + "\n")

    def count_live_neighbors(self, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count

    def next_generation(self):
        new_grid = copy.deepcopy(self.grid)
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)
                if self.grid[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r][c] = 0  # Cell dies
                else:
                    if live_neighbors == 3:
                        new_grid[r][c] = 1  # Cell becomes alive
        self.grid = new_grid

    def run(self, generations=10, delay=1):
        for _ in range(generations):
            self.display()
            self.next_generation()
            time.sleep(delay)

# Example initial states
glider = [(1,2), (2,3), (3,1), (3,2), (3,3)]
blinker = [(2,1), (2,2), (2,3)]
block = [(1,1), (1,2), (2,1), (2,2)]

# Create game instance
game = GameOfLife(rows=10, cols=10, initial_state=glider)

# Run the game
game.run(generations=10, delay=0.5)


# ------ Exercise 2

# ------ Exercise 3

# ------ Exercise 4

# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8

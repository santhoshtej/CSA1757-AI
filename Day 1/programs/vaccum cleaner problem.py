import random

CLEAN = 0
DIRTY = 1
OBSTACLE = -1

class VacuumCleaner:
    def __init__(self, grid_size, start_position):
        self.grid_size = grid_size
        self.position = start_position 
        self.grid = self.generate_grid()

    def generate_grid(self):
        grid = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                if (i, j) == self.position:
                    row.append(CLEAN) 
                else:
                    row.append(random.choice([CLEAN, DIRTY, OBSTACLE])) 
            grid.append(row)
        return grid

    def print_grid(self):
        print("\nVacuum Cleaner Grid:")
        for row in self.grid:
            print(' '.join(['X' if cell == OBSTACLE else str(cell) for cell in row]))
        print("\n")

    def move(self, direction):
        row, col = self.position
        if direction == "up" and row > 0: row -= 1
        elif direction == "down" and row < self.grid_size - 1: row += 1
        elif direction == "left" and col > 0: col -= 1
        elif direction == "right" and col < self.grid_size - 1: col += 1

        if self.grid[row][col] != OBSTACLE:
            self.position = (row, col)
            self.clean()

    def clean(self):
        row, col = self.position
        if self.grid[row][col] == DIRTY:
            self.grid[row][col] = CLEAN
            print(f"Cleaned cell at position: {self.position}")

    def start_cleaning(self):
        print("Starting cleaning process...\n")
        steps = 0
        while any(DIRTY in row for row in self.grid): 
            self.print_grid()
            direction = random.choice(["up", "down", "left", "right"])
            print(f"Vacuum cleaner moving {direction}")
            self.move(direction)
            steps += 1
            if steps > 20: 
                print("Too many steps, stopping to prevent infinite loop.")
                break

        print("\nCleaning finished!")
        self.print_grid()

grid_size = 5
start_position = (2, 2)  

vacuum = VacuumCleaner(grid_size, start_position)
vacuum.start_cleaning()

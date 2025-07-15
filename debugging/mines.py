#!/usr/bin/python3
import random
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    """A simple console-based Minesweeper game."""

    def __init__(self, width=10, height=10, mines=10):
        """
        Initializes the Minesweeper game with a grid and randomly placed mines.
        
        Args:
            width (int): Width of the board.
            height (int): Height of the board.
            mines (int): Number of mines to place.
        """
        self.width = width
        self.height = height
        self.total_cells = width * height
        if mines >= self.total_cells:
            raise ValueError("Number of mines must be less than total cells.")
        self.mines = set(random.sample(range(self.total_cells), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """
        Prints the game board.
        
        Args:
            reveal (bool): If True, shows all mines and numbers. If False, shows hidden cells.
        """
        clear_screen()
        print("   " + " ".join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2} ", end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """
        Counts the number of mines surrounding a given cell.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.

        Returns:
            int: Number of nearby mines.
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """
        Reveals the selected cell. If the cell is empty (0 adjacent mines), recursively reveals neighboring cells.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.

        Returns:
            bool: False if mine is hit, True otherwise.
        """
        if self.revealed[y][x]:
            return True
        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def all_safe_cells_revealed(self):
        """Checks if all non-mine cells are revealed (win condition)."""
        revealed_count = sum(row.count(True) for row in self.revealed)
        return revealed_count == self.total_cells - len(self.mines)

    def play(self):
        """Main game loop."""
        while True:
            self.print_board()
            try:
                x = int(input(f"Enter x coordinate (0-{self.width - 1}): "))
                y = int(input(f"Enter y coordinate (0-{self.height - 1}): "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of range. Try again.")
                    continue
                if self.revealed[y][x]:
                    print("Cell already revealed. Try again.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💥 Game Over! You hit a mine.")
                    break
                if self.all_safe_cells_revealed():
                    self.print_board(reveal=True)
                    print("🎉 Congratulations! You've cleared the minefield!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

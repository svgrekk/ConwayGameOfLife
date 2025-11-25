# board.py

from errors import InvalidGridSizeError


class Board:
    """
    Represents the grid for Conway's Game of Life.

    Internally the grid is stored as a 2D list of integers:
    0 = dead cell, 1 = alive cell.
    """

    def __init__(self, rows: int, cols: int) -> None:
        """
        Initialize a new empty board with the given dimensions.

        :param rows: Number of rows in the grid (must be > 0).
        :param cols: Number of columns in the grid (must be > 0).
        :raises InvalidGridSizeError: If rows or cols are not positive.
        """
        if rows <= 0 or cols <= 0:
            raise InvalidGridSizeError(
                f"Rows and columns must be positive integers, got {rows}x{cols}"
            )

        self.rows = rows
        self.cols = cols
        # 2D list filled with zeros (all cells dead)
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, row: int, col: int, alive: bool = True) -> None:
        """
        Set the state of a single cell on the board.

        :param row: Row index of the cell.
        :param col: Column index of the cell.
        :param alive: True to set the cell as alive, False as dead.
        :raises IndexError: If (row, col) is outside the board boundaries.
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError(
                f"Cell ({row}, {col}) is out of bounds for board {self.rows}x{self.cols}"
            )

        self.grid[row][col] = 1 if alive else 0

    def get_cell(self, row: int, col: int) -> int:
        """
        Get the state of a cell on the board.

        If the cell is outside the board boundaries, this function returns 0.
        This is convenient when counting neighbors: cells outside the grid
        are considered dead by default.

        :param row: Row index of the cell.
        :param col: Column index of the cell.
        :return: 1 if the cell is alive, 0 if dead or out of bounds.
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return 0

        return self.grid[row][col]

    def clear(self) -> None:
        """
        Reset the board by setting all cells to dead (0).
        """
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = 0

    def print(self) -> None:
        """
        Print the board to the console in a human-readable form.

        Alive cells are shown as '█', dead cells as '.'.
        This is just a simple text-based visualization.
        """
        for row in self.grid:
            line = "".join("█" if cell else "." for cell in row)
            print(line)

    def save_to_file(self, filepath: str, generation: int) -> None:
        """
        Append the current board state to a text file.

        Each generation is separated by a header line.
        Cells are written as '1' for alive and '0' for dead.

        :param filepath: Path to the output file.
        :param generation: Current generation number (for logging).
        """
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"--- Generation {generation} ---\n")
            for row in self.grid:
                line = "".join("1" if cell else "0" for cell in row)
                f.write(line + "\n")
            f.write("\n")

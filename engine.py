# engine.py

from typing import Optional

from board import Board
from rules import get_ruleset, RuleFunc


def count_neighbors(board: Board, row: int, col: int) -> int:
    """
    Count the number of alive neighbors around a given cell.

    The neighborhood is the standard 8 surrounding cells:
        (row-1, col-1), (row-1, col), (row-1, col+1),
        (row,   col-1),             , (row,   col+1),
        (row+1, col-1), (row+1, col), (row+1, col+1)

    Cells outside the board boundaries are treated as dead.
    This behavior is implemented in Board.get_cell().

    :param board: The board to inspect.
    :param row: Row index of the target cell.
    :param col: Column index of the target cell.
    :return: Number of alive neighbors (0–8).
    """
    neighbors = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            # Skip the cell itself
            if dr == 0 and dc == 0:
                continue

            neighbors += board.get_cell(row + dr, col + dc)

    return neighbors


def next_generation(board: Board, rule: RuleFunc) -> Board:
    """
    Compute the next generation for the given board using the provided rule.

    The function does not modify the original board. Instead, it creates
    and returns a new Board instance with updated cell states.

    :param board: Current board (current generation).
    :param rule: Rule function (is_alive, neighbors) -> 0 or 1.
    :return: New Board instance representing the next generation.
    """
    new_board = Board(board.rows, board.cols)

    for r in range(board.rows):
        for c in range(board.cols):
            is_alive = board.get_cell(r, c)
            neighbors = count_neighbors(board, r, c)
            new_state = rule(is_alive, neighbors)

            # We can safely write directly into new_board.grid
            # because we know indices are valid.
            new_board.grid[r][c] = new_state

    return new_board


def run_simulation(
    board: Board,
    ruleset_name: str,
    steps: int,
    log_file: Optional[str] = None,
) -> Board:
    """
    Run the Game of Life simulation for a given number of steps.

    For each generation:
        - The board may be written to a log file (if log_file is provided).
        - The next generation is computed using the chosen ruleset.

    :param board: Initial board state.
    :param ruleset_name: Name of the ruleset (e.g. "classic", "highlife").
    :param steps: Number of generations to simulate (must be >= 0).
    :param log_file: Optional path to a log file. If provided, each
                     generation (including the final one) will be appended.
    :return: Board instance representing the final state after all steps.
    """
    rule = get_ruleset(ruleset_name)

    # Log the initial state as generation 0 (optional)
    if log_file is not None:
        board.save_to_file(log_file, generation=0)

    # Perform the requested number of steps
    for gen in range(1, steps + 1):
        board = next_generation(board, rule)

        if log_file is not None:
            board.save_to_file(log_file, generation=gen)

    return board

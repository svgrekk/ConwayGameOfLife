# main.py

import os

from board import Board
from engine import run_simulation
from patterns import load_pattern
from errors import GameOfLifeError


def ask_board_from_user() -> Board:
    """
    Interactively ask the user for board dimensions and initial alive cells.

    The user is first asked to enter the number of rows and columns.
    Then the user can enter coordinates of alive cells in the form "row,col",
    one per line. An empty line finishes the input.
    """
    while True:
        try:
            rows_str = input("Enter number of rows: ").strip()
            cols_str = input("Enter number of columns: ").strip()

            rows = int(rows_str)
            cols = int(cols_str)

            board = Board(rows, cols)
            break
        except ValueError:
            print("Please enter valid integers for rows and columns.")
        except GameOfLifeError as e:
            # For example, InvalidGridSizeError
            print(f"Error creating board: {e}")

    print("\nNow enter alive cell coordinates as 'row,col'.")
    print("Press Enter on an empty line when you are done.\n")

    while True:
        line = input("Cell (or empty to finish): ").strip()
        if not line:
            # Empty line -> stop input
            break

        try:
            row_str, col_str = line.split(",")
            r = int(row_str)
            c = int(col_str)
            board.set_cell(r, c, True)
        except ValueError:
            print("Invalid format. Use 'row,col', for example: 1,2")
        except IndexError as e:
            print(f"Cell is out of bounds: {e}")

    return board


def choose_initial_board() -> Board:
    """
    Ask the user how to obtain the initial board:
        1) Load from a pattern file
        2) Create manually

    Returns a Board instance.
    """
    print("Choose how to initialize the board:")
    print("1) Load pattern from file")
    print("2) Create board manually")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        filepath = input(
            "Enter pattern file path (e.g. configs/glider.pattern): "
        ).strip()
        board = load_pattern(filepath)
    else:
        # Default to manual creation if user types anything else
        board = ask_board_from_user()

    return board


def main() -> None:
    """
    Entry point for the Game of Life application.

    This function:
        - chooses how to initialize the board (file or manual),
        - asks for ruleset,
        - optionally starts an interactive Pygame UI,
        - or runs a console-based simulation with logging.
    """
    print("=== Conway's Game of Life ===\n")

    try:
        # 1) Get initial board (from file or manual input)
        board = choose_initial_board()

        # 2) Ask for ruleset name (default: classic)
        ruleset_name = input(
            "Enter ruleset name (classic/highlife) [default: classic]: "
        ).strip() or "classic"

        # 3) Ask if user wants graphical interactive mode
        use_pygame = input(
            "Run graphical interactive mode with Pygame? (y/n) [n]: "
        ).strip().lower() == "y"

        if use_pygame:
            # Import here so that the program can still run without Pygame installed.
            try:
                from ui_pygame import run_pygame

                print("\nStarting Pygame interactive mode...")
                print("Controls:")
                print("  - LEFT MOUSE BUTTON: toggle a cell (alive/dead)")
                print("  - SPACE: start/stop the simulation (pause/unpause)")
                print("  - C: clear the board (all cells dead)")
                print("  - ESC or window close: exit\n")

                run_pygame(board, ruleset_name)
                # After the window is closed, we simply exit the program.
                return
            except ImportError:
                print(
                    "Pygame is not installed or could not be imported. "
                    "Falling back to console mode.\n"
                )

        # 4) If we are here, run console (non-graphical) simulation

        # Ask for number of generations
        while True:
            steps_str = input("Enter number of generations to simulate: ").strip()
            try:
                steps = int(steps_str)
                if steps < 0:
                    print("Number of generations must be non-negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer for the number of generations.")

        # Prepare log file path (create 'logs' directory if needed)
        logs_dir = "logs"
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, "simulation.log")

        print("\nRunning simulation in console mode...\n")

        final_board = run_simulation(
            board=board,
            ruleset_name=ruleset_name,
            steps=steps,
            log_file=log_file,
        )

        print("Final board state:\n")
        final_board.print()

        print(f"\nSimulation log has been written to: {log_file}")

    except GameOfLifeError as e:
        # Any custom project-related error (patterns, rulesets, grid, etc.)
        print(f"\nGame of Life error: {e}")
    except Exception as e:
        # Any unexpected error (programming bug, etc.)
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()

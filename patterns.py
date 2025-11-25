# patterns.py

import re
from typing import List, Tuple

from board import Board
from errors import PatternParseError

# Regular expression for the SIZE line, e.g.:
#   SIZE 10x20
SIZE_RE = re.compile(r"^SIZE\s+(\d+)x(\d+)\s*$")

# Regular expression for ALIVE lines, e.g.:
#   ALIVE 3,5
ALIVE_RE = re.compile(r"^ALIVE\s+(\d+)\s*,\s*(\d+)\s*$")


def _strip_bom(line: str) -> str:
    """
    Remove UTF-8 BOM (Byte Order Mark) from the beginning of the line if present.

    Some editors (e.g. Windows Notepad) save files with BOM, which can cause
    the first line to start with an invisible character. This breaks simple
    regular expressions like ^SIZE ...
    """
    # \ufeff is the Unicode BOM character
    if line.startswith("\ufeff"):
        return line.lstrip("\ufeff")
    return line


def load_pattern(filepath: str) -> Board:
    """
    Load a pattern from a text file and return a Board instance.

    Expected file format (lines):
        # Comments start with '#'
        SIZE <rows>x<cols>
        ALIVE row,col
        ALIVE row,col
        ...

    Indexing:
        - Rows and columns are zero-based.
        - (0,0) is the top-left cell.

    :param filepath: Path to the pattern file.
    :return: A Board object with the specified alive cells.
    :raises PatternParseError: If the file is missing required lines,
                               contains malformed lines, or is not found.
    """
    rows = None
    cols = None
    alive_cells: List[Tuple[int, int]] = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                original_line = line  # Keep original for error messages

                # First, strip trailing/leading whitespace
                line = line.strip()
                # Then, remove BOM if present
                line = _strip_bom(line)

                # Skip empty lines or comments
                if not line or line.startswith("#"):
                    continue

                # Try to match SIZE line
                m_size = SIZE_RE.match(line)
                if m_size:
                    rows = int(m_size.group(1))
                    cols = int(m_size.group(2))
                    continue

                # Try to match ALIVE line
                m_alive = ALIVE_RE.match(line)
                if m_alive:
                    r = int(m_alive.group(1))
                    c = int(m_alive.group(2))
                    alive_cells.append((r, c))
                    continue

                # If line does not match any known pattern, raise an error
                raise PatternParseError(
                    f"Cannot parse line in pattern file: {original_line.strip()}"
                )

    except FileNotFoundError as e:
        # Wrap the built-in exception in our custom PatternParseError
        raise PatternParseError(f"Pattern file not found: {filepath}") from e

    # After reading the file, we must have SIZE defined
    if rows is None or cols is None:
        raise PatternParseError("Missing SIZE line in pattern file")

    # Create the board and apply all alive cells
    board = Board(rows, cols)
    for r, c in alive_cells:
        try:
            board.set_cell(r, c, True)
        except IndexError as e:
            # If coordinates are outside the board, report a clear error
            raise PatternParseError(
                f"Alive cell ({r}, {c}) is out of bounds for board {rows}x{cols}"
            ) from e

    return board

# ui_pygame.py

import pygame

from board import Board
from engine import next_generation
from rules import get_ruleset


# Size of one cell in pixels
CELL_SIZE = 20

# Colors (R, G, B)
BG_COLOR = (10, 10, 10)
GRID_COLOR = (40, 40, 40)
ALIVE_COLOR = (0, 200, 0)
DEAD_COLOR = BG_COLOR

# Frames per second when simulation is running
FPS = 10


def run_pygame(board: Board, ruleset_name: str) -> None:
    """
    Run an interactive Pygame window for the Game of Life.

    Controls:
        - LEFT MOUSE BUTTON: toggle a cell (alive/dead)
        - SPACE: start/stop the simulation (pause/unpause)
        - C: clear the board (all cells dead)
        - ESC or window close: exit the application
    """
    pygame.init()

    width = board.cols * CELL_SIZE
    height = board.rows * CELL_SIZE

    screen = pygame.display.set_mode((width, height))
    # ✅ Correct function name:
    pygame.display.set_caption("Conway's Game of Life")

    clock = pygame.time.Clock()
    rule = get_ruleset(ruleset_name)

    running = True
    paused = True  # start in paused mode so the user can edit the board first

    while running:
        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Toggle pause state
                    paused = not paused
                elif event.key == pygame.K_c:
                    # Clear the board
                    board.clear()
                elif event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Toggle cell on mouse click
                mouse_x, mouse_y = event.pos
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE

                if 0 <= row < board.rows and 0 <= col < board.cols:
                    current = board.get_cell(row, col)
                    board.set_cell(row, col, alive=(not bool(current)))

        # --- Update simulation ---
        if not paused:
            board = next_generation(board, rule)

        # --- Drawing ---
        screen.fill(BG_COLOR)

        # Draw cells
        for r in range(board.rows):
            for c in range(board.cols):
                rect = pygame.Rect(
                    c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE
                )
                color = ALIVE_COLOR if board.grid[r][c] else DEAD_COLOR
                pygame.draw.rect(screen, color, rect)

        # Draw grid lines (optional)
        for x in range(0, width, CELL_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, height))
        for y in range(0, height, CELL_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (width, y))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

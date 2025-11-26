# ACIT4420 – Final Assignment, Part II


# Conway's Game of Life (Part II)

This repository contains a Conway's Game of Life simulator and forms **Part II** of a two-part final project.  
Part I (courier routing) is provided in a separate repository; this part focuses entirely on cellular automata.

The simulator:

- runs Conway's Game of Life on a finite 2D grid,
- supports loading initial patterns from simple text files,
- offers a console mode for stepping through generations,
- includes an interactive graphical mode built with Pygame (toggling cells, start/pause, clear),
- allows multiple rulesets that are registered through a small decorator-based mechanism.

The code is split into modules for the board representation, rules, pattern loading, simulation engine, user interface and error handling, so the same core logic can be reused in both console and graphical modes.


---

## Files and structure

- `main.py` – entry point, user interaction (menu, mode selection, starting simulation)  
- `board.py` – `Board` class: grid (list of lists) and basic operations (get/set/clear/print/save)  
- `rules.py` – rulesets (`classic`, `highlife`) + `@ruleset` decorator to register new rules dynamically  
- `patterns.py` – reads pattern files from `configs/` using regex (`SIZE`, `ALIVE` lines)  
- `engine.py` – core logic: neighbor counting, next generation, simulation loop  
- `ui_pygame.py` – Pygame-based interactive UI (same engine, different front-end)  
- `errors.py` – custom exceptions (`GameOfLifeError`, `InvalidGridSizeError`, `PatternParseError`, `RuleSetError`)  

Folders:

- `configs/`
  - `board_config` – custom pattern 
- `logs/`
  - `simulation.log` – created when running console mode

---

## Requirements

- Python **3.10+**
- Packages:
  - `pygame`

Example installation (inside your chosen environment):

~~~bash
pip install pygame
~~~

The rest of the project uses only the Python standard library.

---

## Pattern format (`configs/*.pattern`, `configs/board_config`)

Example:

~~~text
SIZE 10x10

ALIVE 1,2
ALIVE 2,3
ALIVE 3,1
ALIVE 3,2
ALIVE 3,3
~~~

- `SIZE <rows>x<cols>` – board dimensions (0-based indices)  
- `ALIVE row,col` – coordinates of alive cells  
- empty lines and lines starting with `#` are ignored  
- invalid lines or out-of-bounds coordinates raise `PatternParseError`.

---

## How to run and use

From the `ConwayGameOfLife` folder:

~~~bash
python main.py
~~~

The program then:

1. Asks how to initialize the board:
   - `1` – load a pattern from file (for example, `configs/board_config`)
   - `2` – create the board manually (enter size and alive cells)
2. Asks for the ruleset name:
   - `classic` (default) or `highlife`
3. Asks whether to start **Pygame** mode (`y/n`).

### Pygame mode (graphical)

- Left mouse button – toggle cell (alive/dead)  
- `SPACE` – start/pause simulation  
- `C` – clear the board  
- `ESC` or close window – exit  

### Console mode

- You enter the number of generations.  
- All generations are written to `logs/simulation.log`.  
- The final board state is printed in the console (`█` = alive, `.` = dead).

# Conway's Game of Life (ACIT4420-1 – Final Assignment, Part II)

This project is **Part II** of the final assignment for  
**ACIT4420-1 – Problem-solving with scripting**.

The code implements Conway’s Game of Life and demonstrates:

- multiple Python modules and clear separation of responsibilities,
- file handling (loading initial board patterns, logging simulation states),
- regular expressions for pattern parsing,
- custom error handling,
- metaprogramming with a decorator-based ruleset registry,
- graphical interaction using Pygame.

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
  - `glider.pattern` – example pattern
  - `board_config` – custom pattern used in this assignment
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

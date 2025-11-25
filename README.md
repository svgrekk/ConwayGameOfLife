# Conway's Game of Life (ACIT4420-1)

This repository contains **Part II** of the final assignment for the course  
**ACIT4420-1 25H – Problem-solving with scripting**.

The task is to implement a simulator for **Conway’s Game of Life** that demonstrates:

- use of multiple Python modules,
- file handling (loading initial patterns, optional logging),
- regular expressions for parsing pattern files,
- custom error handling,
- basic metaprogramming (dynamic registration of rulesets),
- and (optionally) a simple graphical interface using Pygame.

The focus is not on “fancy graphics”, but on code structure, modularity, and use of the required language features.

---

## Project structure

```text
ConwayGameOfLife/
│
├─ main.py           # Entry point: user interaction, mode selection, simulation start
├─ board.py          # Board class (grid representation and simple operations)
├─ rules.py          # Rulesets (classic, highlife) and decorator-based registry
├─ patterns.py       # Loading initial patterns from files using regex
├─ engine.py         # Core simulation logic: neighbors, next generation, run loop
├─ ui_pygame.py      # Optional Pygame UI for interactive visualization
├─ errors.py         # Custom exception classes used across the project
│
├─ configs/
│   └─ glider.pattern   # Example pattern file
│
├─ logs/
│   └─ simulation.log   # Simulation log (created at runtime in console mode)
│
└─ tests/               # (Optional) pytest tests

## Requirements

- Python **3.10+**
- Packages:
  - `pygame`

Example installation (inside your chosen environment):

~~~bash
pip install pygame
~~~

The rest of the project uses only the Python standard library.

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
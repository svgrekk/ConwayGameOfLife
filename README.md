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

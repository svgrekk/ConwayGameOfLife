# rules.py

from typing import Callable, Dict
from errors import RuleSetError

# Type alias for a rule function:
# takes (is_alive, neighbors) and returns 0 or 1
RuleFunc = Callable[[int, int], int]

# Registry for all available rulesets.
# Keys: ruleset name (str)
# Values: rule function (RuleFunc)
RULESETS: Dict[str, RuleFunc] = {}


def ruleset(name: str) -> Callable[[RuleFunc], RuleFunc]:
    """
    Decorator that registers a rule function under a given name.

    Example:

        @ruleset("classic")
        def classic_rule(is_alive: int, neighbors: int) -> int:
            ...

    After decoration, the function is stored in RULESETS[name],
    so it can be retrieved later with get_ruleset(name).
    """
    def decorator(func: RuleFunc) -> RuleFunc:
        RULESETS[name] = func
        return func

    return decorator



@ruleset("classic")
def classic_rule(is_alive: int, neighbors: int) -> int:
    """
    Standard Conway's Game of Life rules.

    - Any live cell with 2 or 3 live neighbors survives.
    - Any dead cell with exactly 3 live neighbors becomes a live cell.
    - All other live cells die in the next generation.
    """
    if is_alive:
        return 1 if neighbors in (2, 3) else 0
    else:
        return 1 if neighbors == 3 else 0


@ruleset("highlife")
def highlife_rule(is_alive: int, neighbors: int) -> int:
    """
    HighLife ruleset (B36/S23):

    - Same as classic Conway, but a dead cell with 6 neighbors
      also becomes alive.
    """
    if is_alive:
        return 1 if neighbors in (2, 3) else 0
    else:
        return 1 if neighbors in (3, 6) else 0


def get_ruleset(name: str) -> RuleFunc:
    """
    Retrieve a ruleset function by name.

    :param name: Name of the ruleset (e.g. "classic", "highlife").
    :return: A rule function that can be used by the engine.
    :raises RuleSetError: If the requested ruleset does not exist.
    """
    try:
        return RULESETS[name]
    except KeyError as e:
        raise RuleSetError(
            f"Unknown ruleset: {name}. Available rulesets: {list(RULESETS.keys())}"
        ) from e

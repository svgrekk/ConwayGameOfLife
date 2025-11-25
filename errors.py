# errors.py

class GameOfLifeError(Exception):
    """
    Base class for all custom exceptions in the Game of Life project.
    Using a common base class makes it easier to catch project-specific errors.
    """
    pass


class InvalidGridSizeError(GameOfLifeError):
    """
    Raised when the user provides invalid grid dimensions (e.g. non-positive values).
    """
    pass


class PatternParseError(GameOfLifeError):
    """
    Raised when there is an error while parsing a pattern file.
    """
    pass


class RuleSetError(GameOfLifeError):
    """
    Raised when there is an issue with a ruleset.
    """
    pass

"""Root-level import wrapper for autograder compatibility.

The autograder imports `from generate_log import generate_log` at the repository root.
This file re-exports the function from lib.generate_log to satisfy that expectation.
"""

from lib.generate_log import generate_log

__all__ = ["generate_log"]

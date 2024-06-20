"""Module providing miscellaneous functions related to printing."""

import platform
import sys
from shutil import get_terminal_size
from typing import Protocol, TypedDict, TypeVar

if int(platform.python_version_tuple()[1]) >= 11:
    # Using typing's Unpack causes pyright warnings.
    # from typing import Unpack
    from typing_extensions import Unpack
else:
    from typing_extensions import Unpack


_T_contra = TypeVar("_T_contra", contravariant=True)


class _File(Protocol[_T_contra]):
    def write(self, s: _T_contra, /) -> object: ...
    def flush(self) -> object: ...


class _PrintKwargs(TypedDict, total=False):
    sep: str | None
    file: _File[str] | None


def yes_no_prompt(question: str, *, default: bool = True) -> bool:
    """Prompts the user for a binary answer.

    Args:
        question: The text that will be shown to the user.
        default: Default value to use if the user just presses enter.

    Returns:
        True for yes, False for no
    """
    choices = " [Y/n]: " if default else " [y/N]: "

    while answer := input(question + choices).lower().strip():
        if answer not in ("y", "n"):
            print("Input invalid, please enter 'y' or 'n'")
            continue
        return answer == "y"

    return default


def clean_print(
    msg: str, fallback: tuple[int, int] = (156, 38), end: str = "\n", **kwargs: Unpack[_PrintKwargs]
) -> None:
    r"""Print the given string to the console and erase any character previously written on the line.

    Args:
        msg: String to print to the console.
        fallback: If using Windows, size of the terminal to use if it cannot be determined by shutil.
        end: What to add at the end of the print. Usually '\n' (new line), or '\r' (back to the start of the line).
        kwargs: Print function kwargs.
    """
    if sys.platform != "win32":
        print("\r\033[K" + msg, end=end, flush=True, **kwargs)
    else:
        print(msg + " " * (get_terminal_size(fallback=fallback).columns - len(msg)), end=end, flush=True, **kwargs)

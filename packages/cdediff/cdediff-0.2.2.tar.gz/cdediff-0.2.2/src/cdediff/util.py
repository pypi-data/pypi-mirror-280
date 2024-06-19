import argparse
import contextlib
import json
import pathlib
import subprocess
import sys
from typing import Any


def load_json(path: str) -> dict[str, Any]:
    try:
        return json.loads(pathlib.Path(path).read_text())
    except json.decoder.JSONDecodeError:
        print(f"Could not decode JSON file {path!r}.")
    except FileNotFoundError:
        print(f"File {path!r} not found.")
    except PermissionError:
        print(f"Could not open file {path!r}.")
    sys.exit()


def _configure_git(eventkeeper: pathlib.Path, python_executable: str, mode: str) -> None:
    subprocess.check_call(
        [  # noqa: S607
            "git",
            "config",
            f"diff.{mode}.command",
            f'FORCE_COLOR=1 "{python_executable}" -m cdediff difftool-git --mode {mode}',
        ],
        cwd=eventkeeper,
        shell=False,  # noqa: S603
    )


def _remove_git_config(eventkeeper: pathlib.Path) -> None:
    for mode in MODES:
        subprocess.run(
            [  # noqa: S607
                "git",
                "config",
                "--unset",
                f"diff.{mode}.command",
            ],
            cwd=eventkeeper,
            shell=False,  # noqa: S603
            check=False,
        )


MODES = ["reg", "event", "all"]
DEFAULT_MODE = MODES[0]


def setup(args: argparse.Namespace) -> None:
    python_executable = sys.executable
    gitattributes = args.eventkeeper / ".gitattributes"

    if args.remove:
        _remove_git_config(args.eventkeeper)

        with contextlib.suppress(FileNotFoundError):
            gitattributes.unlink()

        print("Removed diff handling from event keeper repository.")
    else:
        _configure_git(args.eventkeeper, python_executable, args.mode)

        gitattributes.write_text(f"*.json diff={args.mode}\n")

        print(f"Configured event keeper repository to use {args.mode}-based diff view.")

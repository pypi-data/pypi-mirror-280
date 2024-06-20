import argparse
import contextlib
import itertools
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


def _set_git_config_value(cwd: pathlib.Path, key: str, value: str) -> None:
    subprocess.check_call(
        [  # noqa: S607
            "git",
            "config",
            key,
            value,
        ],
        cwd=cwd,
        shell=False,  # noqa: S603
    )


def _remove_git_config_value(cwd: pathlib.Path, key: str) -> None:
    subprocess.call(
        [  # noqa: S607
            "git",
            "config",
            "--unset",
            key,
        ],
        cwd=cwd,
        shell=False,  # noqa: S603
    )


def _build_config_values(mode: str) -> dict[str, str]:
    python_executable = sys.executable
    difftool_template = f'"{python_executable}" -m cdediff difftool --mode {{mode}} "$LOCAL" "$REMOTE"'
    diffdriver_template = f'FORCE_COLOR=1 "{python_executable}" -m cdediff diffdriver --mode {{mode}}'
    alias_template = '!git -c diff.cdediff.command="{diffdriver}" difftool --tool={mode}'

    return {
        "diff.tool": mode,
        "difftool.prompt": "false",
        "alias.cdediff": "difftool",
        "diff.cdediff.command": diffdriver_template.format(mode=mode),
        **{
            f"alias.{mode}-diff": alias_template.format(
                diffdriver=diffdriver_template.format(mode=mode).replace('"', '\\"'),
                mode=mode,
            )
            for mode in MODES
        },
        **{f"difftool.{mode}.cmd": difftool_template.format(mode=mode) for mode in MODES},
    }


def _get_legacy_config_keys() -> list[str]:
    return list(
        itertools.chain.from_iterable(
            [
                f"diff.{mode}.command",
            ]
            for mode in _LEGACY_MODES
        ),
    )


def _configure_git(eventkeeper: pathlib.Path, mode: str) -> None:
    for key, value in _build_config_values(mode).items():
        _set_git_config_value(eventkeeper, key, value)


def _remove_git_config(eventkeeper: pathlib.Path) -> None:
    for key in _build_config_values(DEFAULT_MODE):  # mode does not matter here.
        _remove_git_config_value(eventkeeper, key)
    for key in _get_legacy_config_keys():
        _remove_git_config_value(eventkeeper, key)


MODES = ["reg", "event", "all"]
_LEGACY_MODES: list[str] = []  # If you remove a mode, add it here, so that it can be cleaned up properly.
DEFAULT_MODE = MODES[0]


def setup(args: argparse.Namespace) -> None:
    gitattributes: pathlib.Path = args.eventkeeper / ".gitattributes"

    _remove_git_config(args.eventkeeper)
    with contextlib.suppress(FileNotFoundError):
        gitattributes.unlink()

    if args.remove:
        print("Removed diff handling from event keeper repository.")
    else:
        _configure_git(args.eventkeeper, args.mode)

        if args.diff:
            gitattributes.write_text("*.json diff=cdediff\n")
            print(f"Configured event keeper repository to use {args.mode}-based diff view.")
        else:
            print("Added difftools and git aliases to event keeper repository.")

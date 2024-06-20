import argparse
import pathlib
import sys

from cdediff.data import Event
from cdediff.util import DEFAULT_MODE, MODES, load_json, setup

global_parser = argparse.ArgumentParser(
    prog="python3 -m cdediff",
)
global_parser.add_argument(
    "--version",
    "-v",
    action="store_true",
)
subparsers = global_parser.add_subparsers(
    title="subcommands",
    dest="subcommand",
)

setup_parser = subparsers.add_parser(
    name="setup",
    help="Configure an eventkeeper repository to use cdediff.",
)
setup_parser.add_argument(
    "eventkeeper",
    action="store",
    type=pathlib.Path,
    help="Path to the eventkeeper repository.",
)
setup_parser.add_argument(
    "--mode",
    choices=MODES,
    default=DEFAULT_MODE,
)
setup_parser.add_argument(
    "--remove",
    action="store_true",
    default=False,
    help="Remove git configuration.",
)
setup_parser.add_argument(
    "--no-diff",
    dest="diff",
    action="store_false",
    default=True,
    help=f"Set `git diff` to use cdediff. This breaks `git difftool --tool=[{'|'.join(MODES)}]`.",
)
setup_parser.set_defaults(func=setup)

textconv_parser = subparsers.add_parser(
    name="textconv",
    help="Convert a CdEDB export into a readable text format.",
)
textconv_parser.add_argument(
    "exportfile",
    action="store",
    type=pathlib.Path,
    help="Path to the CdEDB-Export file.",
)
textconv_parser.add_argument(
    "--mode",
    choices=MODES,
    default=DEFAULT_MODE,
)


def textconv(args: argparse.Namespace) -> None:
    import cdediff.output

    event = Event.from_json(load_json(args.exportfile))

    if args.mode in {"reg", "all"}:
        cdediff.output.print_registrations(event)
    if args.mode in {"event", "all"}:
        cdediff.output.print_event(event)


textconv_parser.set_defaults(func=textconv)


# The difftool is called by `git difftool`, but is also meant for direct use,
#  while the diffdriver is only meant to be called by `git difF`.
#  The only difference(^^) is the number of arguments the take.

difftool_parser = subparsers.add_parser(
    name="difftool",
    help="Compile a detailed report of differences between two CdEDB exports.",
)
difftool_parser.add_argument(
    "old_export",
    action="store",
    type=pathlib.Path,
    help="Path to the old CdEDB export",
)
difftool_parser.add_argument(
    "new_export",
    action="store",
    type=pathlib.Path,
    help="Path to the new CdEDB export",
)
difftool_parser.add_argument(
    "--mode",
    choices=MODES,
    default=DEFAULT_MODE,
)

diffdriver_parser = subparsers.add_parser(
    name="diffdriver",
)
diffdriver_parser.add_argument(
    "path",
    action="store",
    type=pathlib.Path,
)
diffdriver_parser.add_argument(
    "old_export",
    action="store",
    type=pathlib.Path,
    help="Path to the old CdEDB export",
)
diffdriver_parser.add_argument(
    "old_hex",
    action="store",
)
diffdriver_parser.add_argument(
    "old_mode",
    action="store",
)
diffdriver_parser.add_argument(
    "new_export",
    action="store",
    type=pathlib.Path,
    help="Path to the new CdEDB export",
)
diffdriver_parser.add_argument(
    "new_hex",
    action="store",
)
diffdriver_parser.add_argument(
    "new_mode",
    action="store",
)
diffdriver_parser.add_argument(
    "--mode",
    choices=MODES,
    default=DEFAULT_MODE,
)


def difftool(args: argparse.Namespace) -> None:
    import cdediff.output

    old_event = Event.from_json(load_json(args.old_export))
    new_event = Event.from_json(load_json(args.new_export))

    if args.mode in {"reg", "all"}:
        cdediff.output.print_event_registrations_diff(old_event, new_event)
        if args.mode == "all":
            print()
            print("=" * 80)
            print()
    if args.mode in {"event", "all"}:
        cdediff.output.print_event_diff(old_event, new_event)


difftool_parser.set_defaults(func=difftool)
diffdriver_parser.set_defaults(func=difftool)

diffsince_parser = subparsers.add_parser(
    "diffsince",
    help="Show a diff since a specific time.",
)
diffsince_parser.add_argument(
    "date",
    action="store",
    type=str,
    help="The date of the old revision. May be fuzzy like '2 days ago'.",
)
diffsince_parser.add_argument(
    "until",
    action="store",
    type=str,
    default=None,
    nargs="?",
    help="The date of the current revision. May be fuzzy like '1 hour ago'.",
)
diffsince_parser.add_argument(
    "--verbose",
    "-v",
    action="count",
    default=0,
    help="Increase verbosity of output.",
)
diffsince_parser.add_argument(
    "--mode",
    choices=MODES,
    default=DEFAULT_MODE,
)


def diffsince(args: argparse.Namespace) -> None:

    from cdediff.util import get_commit_at_date, get_num_of_commits_between, print_git_diff_between, print_git_log_between

    old_revision = get_commit_at_date(args.date)
    new_revision = get_commit_at_date(args.until)

    print()

    if args.verbose > 2:  # noqa: PLR2004
        print(f"git diff {old_revision}..{new_revision}\n")

    if args.verbose > 0:
        num = get_num_of_commits_between(old_revision, new_revision)
        if num:
            if args.until is None:
                print(f"Found {num} commits since {args.date!r}:")
            else:
                print(f"Found {num} commits between {args.date!r} and {args.until!r}:")
        elif args.until is None:
            print(f"No changes since {args.date!r}.")
        else:
            print(f"No changes between {args.date!r} and {args.until!r}.")
        print()

    if args.verbose > 1:
        print_git_log_between(old_revision, new_revision)
        print()

    print_git_diff_between(old_revision, new_revision, args.mode)
    print()


diffsince_parser.set_defaults(func=diffsince)


args = global_parser.parse_args()

if args.version:
    from importlib.metadata import version

    print(version("cdediff"))
    sys.exit(0)
if not args.subcommand:
    global_parser.print_help()
    sys.exit(1)

sys.stdout.reconfigure(encoding="utf8")  # type: ignore[attr-defined]

args.func(args)

import collections
import contextlib
import datetime
import decimal
import difflib
import io
from collections.abc import Callable
from typing import Literal

import colorama
import termcolor

from cdediff.data import (
    Course,
    CourseSegment,
    Event,
    EventPart,
    EventTrack,
    Lodgement,
    LodgementPart,
    Registration,
    RegistrationPart,
    RegistrationPartStati,
    RegistrationTrack,
)

__all__ = [
    "print_event",
    "print_event_part",
    "print_event_track",
    "print_lodgments",
    "print_lodgement_inhabitants",
    "print_courses",
    "print_course_attendees",
    "print_registration",
    "print_registrations",
    # "print_diff",
    "print_event_diff",
    "print_event_part_diff",
    "print_event_track_diff",
    "print_course_diff",
    "print_course_segment_diff",
    "print_course_segment_attendees_diff",
    "print_lodgement_diff",
    "print_event_registrations_diff",
    "print_reg_part_diff",
    "print_reg_track_diff",
]

colorama.just_fix_windows_console()


def _indent(data: list[str] | str, indent: int, indent_str: str = " " * 4, prefix: str = "") -> str:
    if isinstance(data, str):
        data = data.split("\n") if "\n" in data else [data]
    return prefix + indent_str * indent + ("\n" + prefix + indent_str * indent).join(data)


def format_lodgements(event_part: EventPart) -> list[str]:
    return [str(lodgement_part) for lodgement_part in event_part.lodgements if lodgement_part]


def format_courses(event_track: EventTrack) -> list[str]:
    return [str(course_track) for course_track in event_track.active_courses if course_track]


def format_inhabitants(lodgement_part: LodgementPart) -> list[str]:
    ret = []
    for reg in lodgement_part.inhabitants:
        name = reg.reg.name
        if reg.is_camping_mat:
            name += " (camping mat)"
        ret.append(name)

    return ret


def format_attendees(course_segment: CourseSegment) -> list[str]:
    return [
        attendee.attendee_str + f" {attendee.reg_part.status}" * (attendee.reg_part.status != RegistrationPartStati.participant)
        for attendee in course_segment.attendees
    ]


def print_event(event: Event, indent: int = 0) -> None:
    print(_indent(f"{event}:", indent))

    for event_part in event.parts:
        print_event_part(event_part, indent + 1)


def print_registrations_by_status(event_part: EventPart, indent: int = 0) -> None:
    print(_indent("Participants:", indent))
    for reg in event_part.participants:
        print(_indent(reg.name, indent + 1))

    print(_indent("Waitlist (not in order):", indent))
    for reg in event_part.waitlist:
        print(_indent(reg.name, indent + 1))

    print(_indent("Guests:", indent))
    for reg in event_part.guests:
        print(_indent(reg.name, indent + 1))


def print_event_part(event_part: EventPart, indent: int = 0) -> None:
    print(_indent(f"{event_part}:", indent))

    print(_indent("Lodgements:", indent + 1))
    for lodgement_part in event_part.lodgements:
        if lodgement_part:
            print(_indent(f"{lodgement_part}:", indent + 2))
            print(_indent(format_inhabitants(lodgement_part), indent + 3))

    print(_indent("Courses:", indent + 1))
    for event_track in event_part.tracks:
        print(_indent(f"{event_track}:", indent + 2))
        for course_segment in event_track.active_courses:
            if course_segment:
                if course_segment.attendees or course_segment.instructors:
                    print(_indent(f"{course_segment}:", indent + 3))
                    print(_indent(format_attendees(course_segment), indent + 4))
                else:
                    print(_indent(str(course_segment), indent + 3))

    print_registrations_by_status(event_part, indent + 1)


def print_event_track(event_track: EventTrack, indent: int = 0) -> None:
    print(_indent(f"{event_track}:", indent))
    print(_indent("Courses:", indent + 1))
    print(_indent(format_courses(event_track), indent + 2))


def print_lodgments(event: Event, indent: int = 0) -> None:
    print(_indent("Lodgements:", indent))
    for event_part in event.parts:
        print(_indent(f"{event_part}:", indent + 1))
        print(_indent(format_lodgements(event_part), indent + 2))


def print_lodgement_inhabitants(lodgement: Lodgement, indent: int = 0) -> None:
    print(_indent(f"{lodgement}:", indent))
    for lodgement_part in lodgement.parts:
        if lodgement_part:
            print(_indent(f"{lodgement_part.part} ({lodgement_part.num_reg}+{lodgement_part.num_mat}):", indent + 1))
            print(_indent(format_inhabitants(lodgement_part), indent + 2))


def print_courses(event: Event, indent: int = 0) -> None:
    print(_indent("Courses:", indent))
    for event_track in event.tracks:
        print(_indent(f"{event_track}:", indent + 1))
        print(_indent(format_courses(event_track), indent + 2))


def print_course_attendees(course: Course, indent: int = 0) -> None:
    print(_indent(f"{course}:", indent))
    for course_segment in course.segments:
        if course_segment:
            print(_indent(f"{course_segment.track} ({course_segment.num_att}+{course_segment.num_ins})", indent + 1))
            print(_indent(format_attendees(course_segment), indent + 2))


def print_registration(registration: Registration, indent: int = 0) -> None:
    print(_indent(f"{registration.name}:", indent))
    for registration_part in registration.parts:
        if registration_part.status == RegistrationPartStati.not_applied:
            continue
        print(_indent(f"{registration_part.part}:", indent + 1))
        print(_indent(f"Status: {registration_part.status}", indent + 2))
        if not registration_part.status.is_involved():
            continue
        print(_indent(f"Lodgement: {registration_part.lodgement_str}", indent + 2))
        for event_track in registration_part.part.tracks:
            registration_track = registration.tracks_by_track[event_track]
            print(_indent(f"{event_track}:", indent + 2))
            print(_indent(f"Course: {registration_track.course_str}", indent + 3))
            if registration_track.is_potential_instructor and not registration_track.is_instructor:
                print(_indent(f"Instructed Course: {registration_track.instructed_course}", indent + 3))


def print_registrations(event: Event, indent: int = 0) -> None:
    print(_indent(f"{event.title}:", indent))
    for registration in sorted(event.registrations, key=lambda reg: reg.id):
        print_registration(registration, indent + 1)
        print()


def get_output(fun: Callable[[], None]) -> list[str]:
    with contextlib.redirect_stdout(io.StringIO()) as capture:
        fun()
    return [s + "\n" for s in capture.getvalue().split("\n")]


def print_diff(
    old_lines: list[str],
    new_lines: list[str],
    fromfile: str = "old",
    tofile: str = "new",
    fromfiledate: str = "",
    tofiledate: str = "",
) -> None:
    diffs = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=fromfile,
        tofile=tofile,
        fromfiledate=fromfiledate,
        tofiledate=tofiledate,
    )
    for diff in diffs:
        print(diff, end="")


# def print_event_diff(old_event: Event, new_event: Event) -> None:
#     print_diff(get_output(lambda: print_event(old_event)), get_output(lambda: print_event(new_event)))  # noqa: ERA001

_CONTEXT_QUEUE: dict[int, list[str]] = collections.defaultdict(list)


def _flush_context(indent: int) -> None:
    for level, lines in sorted(_CONTEXT_QUEUE.items()):
        if level < indent:
            for line in lines:
                print(line)
    _CONTEXT_QUEUE.clear()


def context(s: str, indent: int = 0, *, force: bool = False) -> None:
    for level in list(_CONTEXT_QUEUE):
        if indent <= level:
            del _CONTEXT_QUEUE[level]
    text = f" {_indent(s, indent)}"
    if force:
        _CONTEXT_QUEUE[indent - 1].append(text)
    else:
        _CONTEXT_QUEUE[indent].append(text)


def _colored(s: str, color: Literal["red", "green", "cyan"]) -> None:
    for line in s.split("\n"):
        print(termcolor.colored(line, color))


def removed(s: str, indent: int = 0) -> None:
    _flush_context(indent)
    _colored(_indent(s, indent, prefix="-"), "red")


def added(s: str, indent: int = 0) -> None:
    _flush_context(indent)
    _colored(_indent(s, indent, prefix="+"), "green")


def changed(s: str, indent: int = 0) -> None:
    _flush_context(indent)
    _colored(_indent(s, indent, prefix="~"), "cyan")


def print_event_registrations_diff(old_event: Event, new_event: Event) -> None:
    if old_event.id != new_event.id:
        print("#################################################################")
        print("# Comparing different events. This doesn't make a lot of sense! #")
        print("#################################################################")

    if old_event.title == new_event.title:
        context(f"{old_event.title}:")
    else:
        changed(f"{old_event.title} -> {new_event.title}:")

    if old_event.shortname == new_event.shortname:
        context(f"shortname = {old_event.shortname}", 1)
    else:
        changed(f"shortname = {old_event.shortname} -> {new_event.shortname}", 1)

    if not old_event.registrations and not new_event.registrations:
        return

    context("Registrations:", 1)

    old_registration_ids = {reg.id for reg in old_event.registrations}
    new_registration_ids = {reg.id for reg in new_event.registrations}

    added_registrations = sorted(
        new_event.registrations_by_id[reg_id] for reg_id in new_registration_ids - old_registration_ids
    )
    removed_registrations = sorted(
        old_event.registrations_by_id[reg_id] for reg_id in old_registration_ids - new_registration_ids
    )
    other_registrations = sorted(
        old_event.registrations_by_id[reg_id] for reg_id in old_registration_ids & new_registration_ids
    )

    for old_registration in other_registrations:
        new_registration = new_event.registrations_by_id[old_registration.id]
        if old_registration.name == new_registration.name:
            context(f"{old_registration.name}:", 2)
        else:
            changed(f"{old_registration.name} -> {new_registration.name}:", 2)

        print_reg_diff(old_registration, new_registration, 3)

        for old_reg_part in old_registration.parts:
            if new_reg_part := new_registration.parts_by_part_id[old_reg_part.part.id]:
                print_reg_part_diff(old_reg_part, new_reg_part, 3)
            else:
                print_reg_part_diff(old_reg_part, None, 3)
        for new_reg_part in new_registration.parts:
            if new_reg_part.part.id not in new_registration.parts_by_part_id:
                print_reg_part_diff(None, new_reg_part, 3)

    for old_registration in removed_registrations:
        removed(f"{old_registration.name}:", 2)

        print_reg_diff(old_registration, None, 3)

        for old_reg_part in old_registration.parts:
            print_reg_part_diff(old_reg_part, None, 3)
    for new_registration in added_registrations:
        added(f"{new_registration.name}:", 2)

        print_reg_diff(None, new_registration, 3)

        for new_reg_part in new_registration.parts:
            print_reg_part_diff(None, new_reg_part, 3)


def print_reg_diff(
    old_reg: Registration | None,
    new_reg: Registration | None,
    indent: int = 0,
) -> None:
    if old_reg is not None and new_reg is not None:
        print_field_value_diff("notes", old_reg.notes, new_reg.notes, indent)
        print_field_value_diff("orga notes", old_reg.orga_notes, new_reg.orga_notes, indent)
        print_field_value_diff("amount paid", old_reg.amount_paid, new_reg.amount_paid, indent)
        print_field_value_diff("amount owed", old_reg.amount_owed, new_reg.amount_owed, indent)
        print_field_value_diff("remaining owed", old_reg.remaining_owed, new_reg.remaining_owed, indent)
        print_field_value_diff("payment date", old_reg.payment, new_reg.payment, indent)

        context("fields:", indent)
        for field_name, new_value in new_reg.fields.items():
            old_value = old_reg.fields.get(field_name)
            print_field_value_diff(field_name, old_value, new_value, indent + 1)

    elif old_reg is not None:
        print_field_value_diff("notes", old_reg.notes, None, indent)
        print_field_value_diff("orga notes", old_reg.orga_notes, None, indent)
        print_field_value_diff("amount paid", old_reg.amount_paid, None, indent)
        print_field_value_diff("amount owed", old_reg.amount_owed, None, indent)
        print_field_value_diff("remaining owed", old_reg.remaining_owed, None, indent)
        print_field_value_diff("payment date", old_reg.payment, None, indent)

        removed("fields:", indent)
        for field_name, old_value in old_reg.fields.items():
            print_field_value_diff(field_name, old_value, None, indent + 1)

    elif new_reg is not None:
        print_field_value_diff("notes", None, new_reg.notes, indent)
        print_field_value_diff("orga notes", None, new_reg.orga_notes, indent)
        print_field_value_diff("amount paid", None, new_reg.amount_paid, indent)
        print_field_value_diff("amount owed", None, new_reg.amount_owed, indent)
        print_field_value_diff("remaining owed", None, new_reg.remaining_owed, indent)
        print_field_value_diff("payment date", None, new_reg.payment, indent)

        added("fields:", indent)
        for field_name, new_value in new_reg.fields.items():
            print_field_value_diff(field_name, None, new_value, indent + 1)


def print_field_value_diff(
    field_name: str,
    old_value: str | datetime.date | datetime.datetime | decimal.Decimal | None,
    new_value: str | datetime.date | datetime.datetime | decimal.Decimal | None,
    indent: int = 0,
) -> None:
    old_value, new_value = str(old_value), str(new_value)

    if old_value != "None" and new_value != "None":
        if old_value != new_value:
            if "\n" in old_value or "\n" in new_value:
                changed(f"{field_name}:", indent)
                removed(str(old_value), indent + 1)
                added(str(new_value), indent + 1)
            else:
                changed(f"{field_name} = {old_value} -> {new_value}", indent)

    elif old_value != "None":
        if "\n" in old_value:
            removed(f"{field_name}:", indent)
            removed(str(old_value), indent + 1)
        else:
            removed(f"{field_name} = {old_value}", indent)

    elif new_value != "None":
        if "\n" in new_value:
            added(f"{field_name}:", indent)
            added(new_value, indent + 1)
        else:
            added(f"{field_name} = {new_value}", indent)


def print_reg_part_diff(
    old_reg_part: RegistrationPart | None,
    new_reg_part: RegistrationPart | None,
    indent: int = 0,
) -> None:
    if old_reg_part is not None and new_reg_part is not None:
        if old_reg_part.part.shortname == new_reg_part.part.shortname:
            context(f"{old_reg_part.part.shortname}:", indent)
        else:
            changed(f"{old_reg_part.part.shortname} -> {new_reg_part.part.shortname}:", indent)

        if old_reg_part.status == new_reg_part.status:
            context(f"status = {old_reg_part.status}", indent + 1, force=True)
            if old_reg_part.status == RegistrationPartStati.not_applied:
                return
        else:
            status_change = f"status = {old_reg_part.status} -> {new_reg_part.status}"
            if old_reg_part.status.is_present() == new_reg_part.status.is_present():
                changed(status_change, indent + 1)
            elif old_reg_part.status.is_present():
                removed(status_change, indent + 1)
            else:
                added(status_change, indent + 1)

        if old_reg_part.lodgement_str == new_reg_part.lodgement_str:
            context(f"lodgement = {old_reg_part.lodgement_str}", indent + 1)
        elif old_reg_part.lodgement is None:
            added(f"lodgement = {new_reg_part.lodgement_str}", indent + 1)
        elif new_reg_part.lodgement is None:
            removed(f"lodgement = {old_reg_part.lodgement_str}", indent + 1)
        else:
            changed(f"lodgement = {old_reg_part.lodgement_str} -> {new_reg_part.lodgement_str}", indent + 1)

        for old_reg_track in old_reg_part.reg_tracks:
            if new_reg_track := new_reg_part.reg.tracks_by_track_id.get(old_reg_track.track.id):
                print_reg_track_diff(old_reg_track, new_reg_track, indent + 1)
            else:
                print_reg_track_diff(old_reg_track, None, indent + 1)
        for new_reg_track in new_reg_part.reg_tracks:
            if new_reg_track.track.id not in old_reg_part.reg.tracks_by_track_id:
                print_reg_track_diff(None, new_reg_track, indent + 1)

    elif old_reg_part is not None:
        if old_reg_part.status == RegistrationPartStati.not_applied:
            return
        removed(f"{old_reg_part.part.shortname}:", indent)

        removed(f"status = {old_reg_part.status}", indent + 1)
        removed(f"lodgement = {old_reg_part.lodgement_str}", indent + 1)

        for old_reg_track in old_reg_part.reg_tracks:
            print_reg_track_diff(old_reg_track, None, indent + 1)

    elif new_reg_part is not None:
        if new_reg_part.status == RegistrationPartStati.not_applied:
            return
        added(f"{new_reg_part.part.shortname}:", indent)

        added(f"status = {new_reg_part.status}", indent + 1)
        added(f"lodgement = {new_reg_part.lodgement_str}", indent + 1)

        for new_reg_track in new_reg_part.reg_tracks:
            print_reg_track_diff(None, new_reg_track, indent + 1)


def print_reg_track_diff(
    old_reg_track: RegistrationTrack | None,
    new_reg_track: RegistrationTrack | None,
    indent: int = 0,
) -> None:
    if old_reg_track is not None and new_reg_track is not None:
        if old_reg_track.track.shortname == new_reg_track.track.shortname:
            context(f"{old_reg_track.track.shortname}:", indent)
        else:
            changed(f"{old_reg_track.track.shortname} -> {new_reg_track.track.shortname}:", indent)

        if old_reg_track.course_str == new_reg_track.course_str:
            context(f"course = {old_reg_track.course_str}", indent + 1)
        elif old_reg_track.course is not None and new_reg_track.course is not None:
            changed(f"course = {old_reg_track.course_str} -> {new_reg_track.course_str}", indent + 1)
        elif old_reg_track.course is not None:
            removed(f"course = {old_reg_track.course_str}", indent + 1)
        elif new_reg_track.course is not None:
            added(f"course = {new_reg_track.course_str}", indent + 1)

        if str(old_reg_track.instructed_course) == str(new_reg_track.instructed_course):
            if old_reg_track.is_potential_instructor and not old_reg_track.is_instructor:
                context(f"instructed = {old_reg_track.instructed_course}", indent + 1)
        elif old_reg_track.is_potential_instructor and new_reg_track.is_potential_instructor:
            changed(f"instructed = {old_reg_track.instructed_course} -> {new_reg_track.instructed_course}", indent + 1)
        elif old_reg_track.is_potential_instructor:
            removed(f"instructed = {old_reg_track.instructed_course}", indent + 1)
        elif new_reg_track.is_potential_instructor:
            added(f"instructed = {new_reg_track.instructed_course}", indent + 1)

    elif old_reg_track is not None:
        if old_reg_track.course is not None or old_reg_track.is_potential_instructor:
            removed(f"{old_reg_track.track.shortname}:", indent)

            if old_reg_track.course is not None:
                removed(f"course = {old_reg_track.course_str}", indent + 1)

            if old_reg_track.is_potential_instructor and not old_reg_track.is_instructor:
                removed(f"instructed = {old_reg_track.instructed_course}", indent + 1)
    elif new_reg_track is not None:
        if new_reg_track.course is not None or new_reg_track.is_potential_instructor:
            added(f"{new_reg_track.track.shortname}:", indent)

            if new_reg_track.course is not None:
                added(f"course = {new_reg_track.course_str}", indent + 1)

            if new_reg_track.is_potential_instructor and not new_reg_track.is_instructor:
                added(f"instructed = {new_reg_track.instructed_course}", indent + 1)


def print_event_diff(old_event: Event, new_event: Event) -> None:
    if old_event.id != new_event.id:
        print("#################################################################")
        print("# Comparing different events. This doesn't make a lot of sense! #")
        print("#################################################################")

    if old_event.title == new_event.title:
        context(f"{old_event.title}:")
    else:
        changed(f"{old_event.title} -> {new_event.title}:", 1)

    if old_event.shortname == new_event.shortname:
        context(f"shortname = {old_event.shortname}", 1)
    else:
        changed(f"shortname = {old_event.shortname} -> {new_event.shortname}", 1)

    for old_event_part in old_event.parts:
        if new_event_part := new_event.parts_by_id.get(old_event_part.id):
            print_event_part_diff(old_event_part, new_event_part, 1)
        else:
            print_event_part_diff(old_event_part, None, 1)
    for new_event_part in new_event.parts:
        if new_event_part.id not in old_event.parts_by_id:
            print_event_part_diff(None, new_event_part, 1)

    if old_event.courses or new_event.courses:
        context("Courses:", 1)
    for old_course in old_event.courses:
        if new_course := new_event.courses_by_id.get(old_course.id):
            print_course_diff(old_course, new_course, 2)
        else:
            print_course_diff(old_course, None, 2)
    for new_course in new_event.courses:
        if new_course.id not in old_event.courses_by_id:
            print_course_diff(None, new_course, 2)

    if old_event.lodgements or new_event.lodgements:
        context("Lodgements:", 1)
    for old_lodgement in old_event.lodgements:
        if new_lodgement := new_event.lodgements_by_id.get(old_lodgement.id):
            print_lodgement_diff(old_lodgement, new_lodgement, 2)
        else:
            print_lodgement_diff(old_lodgement, None, 2)
    for new_lodgement in new_event.lodgements:
        if new_lodgement.id not in old_event.lodgements_by_id:
            print_lodgement_diff(None, new_lodgement, 2)


def _print_registrations_diff(
    old_registrations_by_id: dict[int, Registration],
    new_registrations_by_id: dict[int, Registration],
    old_registration_ids: set[int],
    new_registration_ids: set[int],
    indent: int = 0,
) -> None:
    added_registrations = sorted(new_registrations_by_id[reg_id] for reg_id in new_registration_ids - old_registration_ids)
    removed_registrations = sorted(old_registrations_by_id[reg_id] for reg_id in old_registration_ids - new_registration_ids)
    other_registrations = sorted(old_registrations_by_id[reg_id] for reg_id in old_registration_ids & new_registration_ids)

    for old_registration in other_registrations:
        new_registration = new_registrations_by_id[old_registration.id]
        if old_registration.name == new_registration.name:
            context(old_registration.name, indent)
        else:
            changed(f"{old_registration.name} -> {new_registration.name}", indent)
    for old_registration in removed_registrations:
        removed(old_registration.name, indent)
    for new_registration in added_registrations:
        added(new_registration.name, indent)


def print_event_part_diff(
    old_event_part: EventPart | None,
    new_event_part: EventPart | None,
    indent: int = 0,
) -> None:
    if old_event_part is not None and new_event_part is not None:
        if old_event_part.shortname == new_event_part.shortname:
            context(f"{old_event_part}:", indent)
        else:
            changed(f"{old_event_part.shortname} -> {new_event_part.shortname}", indent)

        if old_event_part.title == new_event_part.title:
            context(f"title = {old_event_part.title}", indent + 1)
        else:
            changed(f"title = {old_event_part.title} -> {new_event_part.title}", indent + 1)

        if old_event_part.begin == new_event_part.begin:
            context(f"begin = {old_event_part.begin}", indent + 1)
        else:
            changed(f"begin = {old_event_part.begin} -> {new_event_part.begin}", indent + 1)

        if old_event_part.end == new_event_part.end:
            context(f"end = {old_event_part.end}", indent + 1)
        else:
            changed(f"end = {old_event_part.end} -> {new_event_part.end}", indent + 1)

        for old_event_track in old_event_part.tracks:
            if new_event_track := new_event_part.event.tracks_by_id.get(old_event_track.id):
                print_event_track_diff(old_event_track, new_event_track, 2)
            else:
                print_event_track_diff(old_event_track, None, 2)
        for new_event_track in new_event_part.tracks:
            if new_event_track.id not in old_event_part.event.tracks_by_id:
                print_event_track_diff(None, new_event_track, 2)

        context("Participants:", indent + 1)
        _print_registrations_diff(
            old_event_part.event.registrations_by_id,
            new_event_part.event.registrations_by_id,
            {reg.id for reg in old_event_part.participants},
            {reg.id for reg in new_event_part.participants},
            indent + 2,
        )

        context("Waitlist (not in order):", indent + 1)
        _print_registrations_diff(
            old_event_part.event.registrations_by_id,
            new_event_part.event.registrations_by_id,
            {reg.id for reg in old_event_part.waitlist},
            {reg.id for reg in new_event_part.waitlist},
            indent + 2,
        )

        context("Guests:", indent + 1)
        _print_registrations_diff(
            old_event_part.event.registrations_by_id,
            new_event_part.event.registrations_by_id,
            {reg.id for reg in old_event_part.guests},
            {reg.id for reg in new_event_part.guests},
            indent + 2,
        )

    elif old_event_part is not None:
        removed(f"{old_event_part}:", indent)
        removed(f"title = {old_event_part.title}", indent + 1)
        removed(f"begin = {old_event_part.begin}", indent + 1)
        removed(f"end = {old_event_part.end}", indent + 1)

        for old_event_track in old_event_part.tracks:
            print_event_track_diff(old_event_track, None, 2)

        removed("Participants:", indent + 1)
        for reg in old_event_part.participants:
            removed(reg.name, indent + 2)

        removed("Waitlist (not in order):", indent)
        for reg in old_event_part.waitlist:
            removed(reg.name, indent + 2)

        removed("Guests:", indent)
        for reg in old_event_part.guests:
            removed(reg.name, indent + 2)

    elif new_event_part is not None:
        added(f"{new_event_part}:", indent)
        added(f"title = {new_event_part.title}", indent + 1)
        added(f"begin = {new_event_part.begin}", indent + 1)
        added(f"end = {new_event_part}", indent + 1)

        for new_event_track in new_event_part.tracks:
            print_event_track_diff(None, new_event_track, 2)

        added("Participants:", indent + 1)
        for reg in new_event_part.participants:
            added(reg.name, indent + 2)

        added("Waitlist (not in order):", indent)
        for reg in new_event_part.waitlist:
            added(reg.name, indent + 2)

        added("Guests:", indent)
        for reg in new_event_part.guests:
            added(reg.name, indent + 2)


def print_event_track_diff(old_event_track: EventTrack | None, new_event_track: EventTrack | None, indent: int = 0) -> None:
    if old_event_track is not None and new_event_track is not None:
        if old_event_track.shortname == new_event_track.shortname:
            context(f"{old_event_track}:", indent)
        else:
            changed(f"{old_event_track.shortname} -> {new_event_track.shortname}:", indent)

        if old_event_track.title == new_event_track.title:
            context(f"title = {old_event_track.title}", indent + 1)
        else:
            changed(f"title = {old_event_track.title}", indent + 1)

        if old_event_track.min_choices == new_event_track.min_choices:
            context(f"min choices = {old_event_track.min_choices}", indent + 1)
        else:
            changed(f"min choices = {old_event_track.min_choices} -> {new_event_track.min_choices}", indent + 1)

        if old_event_track.num_choices == new_event_track.num_choices:
            context(f"num choices = {old_event_track.num_choices}", indent + 1)
        else:
            changed(f"num choices = {old_event_track.num_choices} -> {new_event_track.num_choices}", indent + 1)

    elif old_event_track is not None:
        removed(f"{old_event_track}:", indent)
        removed(f"title = {old_event_track.title}", indent + 1)
        removed(f"min_choices = {old_event_track.min_choices}", indent + 1)
        removed(f"num_choices = {old_event_track.num_choices}", indent + 1)
    elif new_event_track is not None:
        added(f"{new_event_track}:", indent)
        added(f"title = {new_event_track.title}", indent + 1)
        added(f"min_choices = {new_event_track.min_choices}", indent + 1)
        added(f"num_choices = {new_event_track.num_choices}", indent + 1)


def print_course_diff(old_course: Course | None, new_course: Course | None, indent: int = 0) -> None:
    if old_course is not None and new_course is not None:
        if str(old_course) == str(new_course):
            context(f"{old_course}:", indent)
        else:
            changed(f"{old_course} -> {new_course}:", indent)

        if old_course.title == new_course.title:
            context(f"title = {old_course.title}", indent + 1)
        else:
            changed(f"title = {old_course.title} -> {new_course.title}", indent + 1)

        for old_course_segment in old_course.segments:
            if (new_course_segment := new_course.segments_by_track_id.get(old_course_segment.track.id)) is not None:
                print_course_segment_diff(old_course_segment, new_course_segment, indent + 1)
            else:
                print_course_segment_diff(old_course_segment, None, indent + 1)
        for new_course_segment in new_course.segments:
            if new_course_segment.track.id not in old_course.segments_by_track_id:
                print_course_segment_diff(None, new_course_segment, indent + 1)

    elif old_course is not None:
        removed(str(old_course), indent)
        removed(f"title = {old_course.title}", indent + 1)
        for segment in old_course.segments:
            print_course_segment_diff(segment, None, indent + 1)

    elif new_course is not None:
        added(f"{new_course}:", indent)
        added(f"title = {new_course.title}", indent + 1)
        for segment in new_course.segments:
            print_course_segment_diff(None, segment, indent + 1)


def print_course_segment_diff(old_segment: CourseSegment | None, new_segment: CourseSegment | None, indent: int = 0) -> None:
    if old_segment is not None and new_segment is not None:
        old_event_track = old_segment.track
        new_event_track = new_segment.track

        if old_event_track.shortname == new_event_track.shortname:
            context(f"{old_event_track.shortname}:", indent)
        else:
            changed(f"{old_event_track.shortname} -> {new_event_track.shortname}:", indent)

        if old_segment.is_active == new_segment.is_active:
            if not old_segment.is_active:
                context("(inactive)", indent + 1)
        elif old_segment.is_active:
            added("(inactive)", indent + 1)
        elif new_segment.is_active:
            removed("(inactive)", indent + 1)

        if old_segment.num_ins == new_segment.num_ins:
            context(f"#Instructors = {old_segment.num_ins}", indent + 1)
        else:
            changed(f"#Instructors = {old_segment.num_ins} -> {new_segment.num_ins}", indent + 1)

        if old_segment.num_att == new_segment.num_att:
            context(f"#Attendees = {old_segment.num_att}", indent + 1)
        else:
            changed(f"#Attendees = {old_segment.num_att} -> {new_segment.num_att}", indent + 1)

        print_course_segment_attendees_diff(old_segment, new_segment, indent + 1)

    elif old_segment is not None:
        removed(f"{old_segment.track.shortname}:", indent)

        if not old_segment.is_active:
            removed("(inactive)", indent + 1)

        removed(f"#Instructors = {old_segment.num_ins}", indent + 1)
        removed(f"#Attendees = {old_segment.num_att}", indent + 1)

        print_course_segment_attendees_diff(old_segment, None, indent + 1)

    elif new_segment is not None:
        added(f"{new_segment.track.shortname}:", indent)

        if not new_segment.is_active:
            added("(inactive)", indent + 1)

        added(f"#Instructors = {new_segment.num_ins}", indent + 1)
        added(f"#Attendees = {new_segment.num_att}", indent + 1)

        print_course_segment_attendees_diff(None, new_segment, indent + 1)


def print_course_segment_attendees_diff(
    old_segment: CourseSegment | None,
    new_segment: CourseSegment | None,
    indent: int = 0,
) -> None:
    if old_segment is not None and new_segment is not None:
        if old_segment.num_att or new_segment.num_att:
            context("Attendees:", indent)

            old_attendee_ids = {attendee.reg.id for attendee in old_segment.attendees}
            new_attendee_ids = {attendee.reg.id for attendee in new_segment.attendees}

            added_attendees = sorted(
                new_segment.attendees_by_registration_id[reg_id] for reg_id in new_attendee_ids - old_attendee_ids
            )
            removed_attendees = sorted(
                old_segment.attendees_by_registration_id[reg_id] for reg_id in old_attendee_ids - new_attendee_ids
            )
            other_attendees = sorted(
                old_segment.attendees_by_registration_id[reg_id] for reg_id in old_attendee_ids & new_attendee_ids
            )

            for old_attendee in other_attendees:
                new_attendee = new_segment.attendees_by_registration_id[old_attendee.reg.id]
                if old_attendee.is_instructor == new_attendee.is_instructor:
                    context(old_attendee.attendee_str, indent + 1)
                else:
                    removed(old_attendee.attendee_str, indent + 1)
                    added(new_attendee.attendee_str, indent + 1)
            for old_attendee in removed_attendees:
                removed(old_attendee.attendee_str, indent + 1)
            for new_attendee in added_attendees:
                added(new_attendee.attendee_str, indent + 1)

    elif old_segment is not None:
        if old_segment.attendees:
            removed("Attendees:", indent)
        for old_attendee in old_segment.attendees:
            removed(old_attendee.attendee_str, indent + 1)

    elif new_segment is not None:
        if new_segment.attendees:
            added("Attendees:", indent)
        for new_attendee in new_segment.attendees:
            added(new_attendee.attendee_str, indent + 1)


def print_lodgement_diff(old_lodgement: Lodgement | None, new_lodgement: Lodgement | None, indent: int = 0) -> None:
    if old_lodgement is not None and new_lodgement is not None:
        if str(old_lodgement) == str(new_lodgement):
            context(f"{old_lodgement}:", indent)
        else:
            changed(f"{old_lodgement} -> {new_lodgement}:", indent)

        if old_lodgement.regular_capacity == new_lodgement.regular_capacity:
            context(f"regular capacity = {old_lodgement.regular_capacity}", indent + 1)
        else:
            changed(f"regular capacity = {old_lodgement.regular_capacity} -> {new_lodgement.regular_capacity}", indent + 1)

        if old_lodgement.camping_mat_capacity == new_lodgement.camping_mat_capacity:
            context(f"camping mat capacity = {old_lodgement.camping_mat_capacity}", indent + 1)
        else:
            changed(
                f"camping mat capacity = {old_lodgement.camping_mat_capacity} -> {new_lodgement.camping_mat_capacity}",
                indent + 1,
            )

        for old_lodge_part in old_lodgement.parts:
            if (new_lodge_part := new_lodgement.parts_by_part_id.get(old_lodge_part.part.id)) is not None:
                print_lodgement_part_diff(old_lodge_part, new_lodge_part, indent + 1)
            else:
                print_lodgement_part_diff(old_lodge_part, None, indent + 1)
        for new_lodge_part in new_lodgement.parts:
            if new_lodge_part.part.id not in old_lodgement.parts_by_part_id:
                print_lodgement_part_diff(None, new_lodge_part, indent + 1)

    elif old_lodgement is not None:
        removed(f"{old_lodgement}:", indent)
        removed(f"regular capacity = {old_lodgement.regular_capacity}", indent + 1)
        removed(f"camping mat capacity = {old_lodgement.camping_mat_capacity}", indent + 1)

        for old_lodge_part in old_lodgement.parts:
            print_lodgement_part_diff(old_lodge_part, None, indent + 1)

    elif new_lodgement is not None:
        added(f"{new_lodgement}:", indent)
        added(f"regular capacity = {new_lodgement.regular_capacity}", indent + 1)
        added(f"camping mat capacity = {new_lodgement.camping_mat_capacity}", indent + 1)

        for new_lodge_part in new_lodgement.parts:
            print_lodgement_part_diff(None, new_lodge_part, indent + 1)


def print_lodgement_part_diff(
    old_lodgement_part: LodgementPart | None,
    new_lodgement_part: LodgementPart | None,
    indent: int = 0,
) -> None:
    if old_lodgement_part is not None and new_lodgement_part is not None:
        if not old_lodgement_part and not new_lodgement_part:
            return
        if old_lodgement_part.part.shortname == new_lodgement_part.part.shortname:
            context(f"{old_lodgement_part.part.shortname}:", indent)
        else:
            changed(f"{old_lodgement_part.part.shortname} -> {new_lodgement_part.part.shortname}):", indent)

        if old_lodgement_part.num_reg == new_lodgement_part.num_reg:
            context(f"#Regular Inhabitants = {old_lodgement_part}", indent + 1)
        else:
            changed(f"#Regular Inhabitants = {old_lodgement_part.num_reg} -> {new_lodgement_part.num_reg}", indent + 1)

        if old_lodgement_part.num_mat == new_lodgement_part.num_mat:
            context(f"#Camping Mat Inhabitants = {old_lodgement_part.num_mat}", indent + 1)
        else:
            changed(f"#Camping Mat Inhabitanta = {old_lodgement_part.num_mat} -> {new_lodgement_part.num_mat}", indent + 1)

        context("Inhabitants:", indent + 1)
        for old_inhabitant in old_lodgement_part.inhabitants:
            if new_inhabitant := new_lodgement_part.inhabitants_by_id.get(old_inhabitant.reg.id):
                if old_inhabitant.inhabitant_str == new_inhabitant.inhabitant_str:
                    context(old_inhabitant.inhabitant_str, indent + 2)
                else:
                    changed(f"{old_inhabitant.inhabitant_str} -> {new_inhabitant.inhabitant_str}", indent + 2)
            else:
                removed(old_inhabitant.inhabitant_str, indent + 2)
        for new_inhabitant in new_lodgement_part.inhabitants:
            if new_inhabitant.reg.id not in old_lodgement_part.inhabitants_by_id:
                added(new_inhabitant.inhabitant_str, indent + 2)

    elif old_lodgement_part is not None:
        if not old_lodgement_part:
            return
        removed(f"{old_lodgement_part.part.shortname}:", indent)

        removed(f"#Regular Inhabitants = {old_lodgement_part.num_reg}", indent + 1)
        removed(f"#Camping Mat Inhabitants = {old_lodgement_part.num_reg}", indent + 1)

        removed("Inhabitants", indent + 1)
        for reg_part in old_lodgement_part.inhabitants:
            removed(reg_part.inhabitant_str, indent + 2)

    elif new_lodgement_part is not None:
        if not new_lodgement_part:
            return
        added(f"{new_lodgement_part.part.shortname}:", indent)

        added(f"#Regular Inhabitants = {new_lodgement_part.num_reg}", indent + 1)
        added(f"#Camping Mat Inhabitants = {new_lodgement_part.num_reg}", indent + 1)

        added("Inhabitants:", indent + 1)
        for reg_part in new_lodgement_part.inhabitants:
            added(reg_part.inhabitant_str, indent + 2)

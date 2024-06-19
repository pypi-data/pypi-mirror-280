import dataclasses
import datetime
import decimal
import enum
import functools
from typing import Any


@dataclasses.dataclass
class Event:
    id: int
    title: str
    shortname: str

    parts: list["EventPart"] = dataclasses.field(repr=False, compare=False)

    @functools.cached_property
    def parts_by_id(self) -> dict[int, "EventPart"]:
        return {part.id: part for part in self.parts}

    @functools.cached_property
    def tracks(self) -> list["EventTrack"]:
        return sorted(sum((part.tracks for part in self.parts), start=[]))  # noqa: RUF017

    @functools.cached_property
    def tracks_by_id(self) -> dict[int, "EventTrack"]:
        return {track.id: track for track in self.tracks}

    courses: list["Course"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    lodgement_groups: list["LodgementGroup"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def lodgement_groups_by_id(self) -> dict[int, "LodgementGroup"]:
        return {group.id: group for group in self.lodgement_groups}

    lodgements: list["Lodgement"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def lodgements_by_id(self) -> dict[int, "Lodgement"]:
        return {lodgement.id: lodgement for lodgement in self.lodgements}

    @functools.cached_property
    def courses_by_id(self) -> dict[int, "Course"]:
        return {course.id: course for course in self.courses}

    registrations: list["Registration"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def registrations_by_id(self) -> dict[int, "Registration"]:
        return {registration.id: registration for registration in self.registrations}

    def sort(self) -> None:
        self.parts.sort()
        for event_part in self.parts:
            event_part.sort()
        self.courses.sort()
        for course in self.courses:
            course.sort()
        self.lodgement_groups.sort()
        for lodgement_group in self.lodgement_groups:
            lodgement_group.sort()
        self.lodgements.sort()
        for lodgement in self.lodgements:
            lodgement.sort()
        self.registrations.sort()

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "Event":
        ret = cls(
            id=data["id"],
            title=data["event"]["title"].strip(),
            shortname=data["event"]["shortname"].strip(),
            parts=sorted(EventPart.from_json(int(part_id), part_data) for part_id, part_data in data["event"]["parts"].items()),
        )

        for event_part in ret.parts:
            event_part.event = ret
        for event_track in ret.tracks:
            event_track.event = ret

        ret.courses = sorted(
            Course.from_json(ret, int(course_id), course_data) for course_id, course_data in data["courses"].items()
        )
        ret.lodgement_groups = sorted(
            LodgementGroup.from_json(int(group_id), group_data) for group_id, group_data in data["lodgement_groups"].items()
        )
        ret.lodgements = sorted(
            Lodgement.from_json(ret, int(lodgement_id), lodgement_data)
            for lodgement_id, lodgement_data in data["lodgements"].items()
        )
        ret.registrations = sorted(
            Registration.from_json(ret, int(reg_id), reg_data) for reg_id, reg_data in data["registrations"].items()
        )

        ret.sort()
        return ret

    def __str__(self) -> str:
        return f"Event({self.title})"


@dataclasses.dataclass
class EventPart:
    event: "Event" = dataclasses.field(init=False, default=None)  # type: ignore[assignment]

    id: int
    title: str
    shortname: str

    begin: datetime.date
    end: datetime.date

    tracks: list["EventTrack"] = dataclasses.field(repr=False, compare=False)

    lodgements: list["LodgementPart"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def participants(self) -> list["Registration"]:
        return [reg for reg in self.event.registrations if reg.parts_by_part[self].status == RegistrationPartStati.participant]

    @functools.cached_property
    def waitlist(self) -> list["Registration"]:
        return [reg for reg in self.event.registrations if reg.parts_by_part[self].status == RegistrationPartStati.waitlist]

    @functools.cached_property
    def guests(self) -> list["Registration"]:
        return [reg for reg in self.event.registrations if reg.parts_by_part[self].status == RegistrationPartStati.guest]

    def sort(self) -> None:
        self.lodgements.sort()
        self.tracks.sort()
        for event_track in self.tracks:
            event_track.sort()

    @classmethod
    def from_json(cls, part_id: int, data: dict[str, Any]) -> "EventPart":
        ret = cls(
            id=part_id,
            title=data["title"].strip(),
            shortname=data["shortname"].strip(),
            begin=datetime.date.fromisoformat(data["part_begin"]),
            end=datetime.date.fromisoformat(data["part_end"]),
            tracks=[EventTrack.from_json(int(track_id), track_data) for track_id, track_data in data["tracks"].items()],
        )

        for event_track in ret.tracks:
            event_track.part = ret

        return ret

    def __hash__(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f"Part({self.shortname})"

    def __lt__(self, other: "EventPart") -> bool:
        return (self.begin, self.end, self.shortname) < (other.begin, other.end, other.shortname)


@dataclasses.dataclass
class EventTrack:
    event: "Event" = dataclasses.field(init=False, default=None)  # type: ignore[assignment]
    part: "EventPart" = dataclasses.field(init=False, default=None)  # type: ignore[assignment]

    id: int
    title: str
    shortname: str

    sortkey: int

    num_choices: int
    min_choices: int

    active_courses: list["CourseSegment"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    def sort(self) -> None:
        self.active_courses.sort()

    @classmethod
    def from_json(cls, track_id: int, data: dict[str, Any]) -> "EventTrack":
        return cls(
            id=track_id,
            title=data["title"].strip(),
            shortname=data["shortname"].strip(),
            sortkey=data["sortkey"],
            num_choices=data["num_choices"],
            min_choices=data["min_choices"],
        )

    def __hash__(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f"Track({self.shortname})"

    def __lt__(self, other: "EventTrack") -> bool:
        return (self.sortkey, self.title) < (other.sortkey, other.title)


@dataclasses.dataclass
class Course:
    event: "Event"
    id: int
    title: str
    shortname: str

    nr: str
    description: str = dataclasses.field(repr=False, compare=False)
    instructors: str = dataclasses.field(repr=False, compare=False)

    min_size: int = dataclasses.field(repr=False, compare=False)
    max_size: int = dataclasses.field(repr=False, compare=False)

    segments: list["CourseSegment"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def segments_by_track(self) -> dict["EventTrack", "CourseSegment"]:
        self.sort()
        return {segment.track: segment for segment in self.segments}

    @functools.cached_property
    def segments_by_track_id(self) -> dict[int, "CourseSegment"]:
        self.sort()
        return {segment.track.id: segment for segment in self.segments}

    @functools.cached_property
    def active_segments(self) -> dict["EventTrack", "CourseSegment"]:
        self.sort()
        return {segment.track: segment for segment in self.segments if segment.is_active}

    def sort(self) -> None:
        self.segments.sort()
        for segment in self.segments:
            segment.sort()

    @classmethod
    def from_json(cls, event: "Event", course_id: int, data: dict[str, Any]) -> "Course":
        ret = cls(
            event=event,
            id=course_id,
            title=data["title"].strip(),
            shortname=data["shortname"].strip(),
            nr=data["nr"].strip(),
            description=data["description"] or "",
            instructors=data["instructors"] or "",
            min_size=data["min_size"] or -1,
            max_size=data["max_size"] or -1,
        )
        ret.segments = sorted(
            CourseSegment(ret, event.tracks_by_id[int(track_id)], is_active) for track_id, is_active in data["segments"].items()
        )

        return ret

    def __str__(self) -> str:
        return f"{self.nr}. {self.shortname}"

    def __lt__(self, other: "Course") -> bool:
        return (self.nr, self.shortname) < (other.nr, self.shortname)


@dataclasses.dataclass
class CourseSegment:
    course: "Course"
    track: "EventTrack"
    is_active: bool

    attendees: list["RegistrationTrack"] = dataclasses.field(default_factory=list, repr=False, compare=False)
    potential_instructors: list["RegistrationTrack"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def instructors(self) -> list["RegistrationTrack"]:
        self.sort()
        return [attendee for attendee in self.attendees if attendee.is_instructor]

    @functools.cached_property
    def num_att(self) -> int:
        return len(self.attendees)

    @functools.cached_property
    def num_ins(self) -> int:
        return len(self.instructors)

    @functools.cached_property
    def attendees_by_registration_id(self) -> dict[int, "RegistrationTrack"]:
        self.sort()
        return {attendee.reg.id: attendee for attendee in self.attendees}

    def __post_init__(self) -> None:
        if self.is_active:
            self.track.active_courses.append(self)

    def sort(self) -> None:
        self.attendees.sort()
        self.potential_instructors.sort()

    def __bool__(self) -> bool:
        return self.is_active or (bool(self.attendees) or bool(self.instructors))

    def __str__(self) -> str:
        ret = f"{self.course} ({len(self.attendees)}+{len(self.instructors)})"
        if not self.is_active:
            ret += " (inactive)"
        return ret

    def __lt__(self, other: "CourseSegment") -> bool:
        return (self.course, self.track) < (other.course, other.track)


@dataclasses.dataclass
class LodgementGroup:
    id: int
    title: str

    lodgements: list["Lodgement"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    def sort(self) -> None:
        self.lodgements.sort()

    @classmethod
    def from_json(cls, group_id: int, data: dict[str, Any]) -> "LodgementGroup":
        return cls(
            id=group_id,
            title=data["title"].strip(),
        )

    def __lt__(self, other: "LodgementGroup") -> bool:
        return (self.title, self.id) < (other.title, other.id)


@dataclasses.dataclass
class Lodgement:
    id: int
    title: str

    regular_capacity: int
    camping_mat_capacity: int

    @property
    def total_capacity(self) -> int:
        return self.regular_capacity + self.camping_mat_capacity

    group: "LodgementGroup"

    parts: list["LodgementPart"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def parts_by_part(self) -> dict["EventPart", "LodgementPart"]:
        self.sort()
        return {part.part: part for part in self.parts}

    @functools.cached_property
    def parts_by_part_id(self) -> dict[int, "LodgementPart"]:
        self.sort()
        return {part.part.id: part for part in self.parts}

    def sort(self) -> None:
        self.parts.sort()

    @classmethod
    def from_json(cls, event: Event, lodgement_id: int, data: dict[str, Any]) -> "Lodgement":
        ret = cls(
            id=lodgement_id,
            title=data["title"].strip(),
            group=event.lodgement_groups_by_id[data["group_id"]],
            regular_capacity=data["regular_capacity"],
            camping_mat_capacity=data["camping_mat_capacity"],
        )
        ret.parts = sorted(LodgementPart(ret, part) for part in event.parts)
        return ret

    def __str__(self) -> str:
        return f"{self.group.title} {self.title}"

    def __lt__(self, other: "Lodgement") -> bool:
        return (self.group, self.title, self.id) < (other.group, other.title, other.id)


@dataclasses.dataclass
class LodgementPart:
    lodgement: "Lodgement"
    part: "EventPart"

    inhabitants: list["RegistrationPart"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def inhabitants_by_id(self) -> dict[int, "RegistrationPart"]:
        self.sort()
        return {reg_part.reg.id: reg_part for reg_part in self.inhabitants}

    @functools.cached_property
    def regular_inhabitants(self) -> list["RegistrationPart"]:
        self.sort()
        return [reg_part for reg_part in self.inhabitants if not reg_part.is_camping_mat]

    @functools.cached_property
    def num_reg(self) -> int:
        return len(self.regular_inhabitants)

    @functools.cached_property
    def camping_mat_inhabitants(self) -> list["RegistrationPart"]:
        self.sort()
        return [reg_part for reg_part in self.inhabitants if reg_part.is_camping_mat]

    @functools.cached_property
    def num_mat(self) -> int:
        return len(self.camping_mat_inhabitants)

    def __post_init__(self) -> None:
        self.part.lodgements.append(self)

    def sort(self) -> None:
        self.inhabitants.sort()

    def __bool__(self) -> bool:
        return bool(self.inhabitants)

    def __str__(self) -> str:
        return f"{self.lodgement} ({self.num_reg}+{self.num_mat})"

    def __lt__(self, other: "LodgementPart") -> bool:
        return (self.lodgement, self.part) < (other.lodgement, other.part)


@dataclasses.dataclass
class Registration:
    id: int
    given_names: str
    display_name: str
    family_name: str

    @property
    def name(self) -> str:
        return f"{self.display_name} {self.family_name}"

    email: str
    notes: str | None
    orga_notes: str | None

    amount_paid: decimal.Decimal
    amount_owed: decimal.Decimal

    @property
    def remaining_owed(self) -> decimal.Decimal:
        return self.amount_owed - self.amount_paid

    payment: datetime.date | None

    fields: dict[str, Any]

    parts: list["RegistrationPart"] = dataclasses.field(default_factory=list, repr=False, compare=False)
    tracks: list["RegistrationTrack"] = dataclasses.field(default_factory=list, repr=False, compare=False)

    @functools.cached_property
    def parts_by_part(self) -> dict["EventPart", "RegistrationPart"]:
        self.sort()
        return {part.part: part for part in self.parts}

    @functools.cached_property
    def parts_by_part_id(self) -> dict[int, "RegistrationPart"]:
        self.sort()
        return {part.part.id: part for part in self.parts}

    @functools.cached_property
    def tracks_by_track(self) -> dict["EventTrack", "RegistrationTrack"]:
        self.sort()
        return {track.track: track for track in self.tracks}

    @functools.cached_property
    def tracks_by_track_id(self) -> dict[int, "RegistrationTrack"]:
        self.sort()
        return {track.track.id: track for track in self.tracks}

    def sort(self) -> None:
        self.parts.sort()
        self.tracks.sort()

    @classmethod
    def from_json(cls, event: "Event", registration_id: int, data: dict) -> "Registration":
        ret = cls(
            id=registration_id,
            given_names=data["persona"]["given_names"].strip(),
            display_name=data["persona"]["display_name"].strip(),
            family_name=data["persona"]["family_name"].strip(),
            email=data["persona"]["username"].strip(),
            notes=data["notes"] or None,
            orga_notes=data["orga_notes"] or None,
            amount_paid=decimal.Decimal(data["amount_paid"]),
            amount_owed=decimal.Decimal(data["amount_owed"]),
            payment=datetime.date.fromisoformat(data["payment"]) if data["payment"] else None,
            fields=(data["fields"] or {}),
        )

        ret.parts = sorted(
            RegistrationPart.from_json(event, ret, event.parts_by_id[int(part_id)], part_data)
            for part_id, part_data in data["parts"].items()
        )

        ret.tracks = sorted(
            RegistrationTrack.from_json(event, ret, event.tracks_by_id[int(track_id)], track_data)
            for track_id, track_data in data["tracks"].items()
        )

        return ret

    def __lt__(self, other: "Registration") -> bool:
        return (self.name, self.id) < (other.name, other.id)


@dataclasses.dataclass
class RegistrationPart:
    reg: "Registration"
    part: "EventPart"
    status: "RegistrationPartStati"

    is_camping_mat: bool
    lodgement: Lodgement | None

    @property
    def lodgement_str(self) -> str:
        return f"{self.lodgement or '–'}" + " (camping mat)" * self.is_camping_mat

    @property
    def inhabitant_str(self) -> str:
        if self.lodgement is None:
            return "–"
        return (
            f"{self.reg.name}"
            + " (camping mat)" * self.is_camping_mat
            + f" ({self.status})" * (self.status != RegistrationPartStati.participant)
        )

    @functools.cached_property
    def reg_tracks(self) -> list["RegistrationTrack"]:
        return [self.reg.tracks_by_track[event_track] for event_track in self.part.tracks]

    @classmethod
    def from_json(cls, event: "Event", reg: "Registration", part: "EventPart", data: dict) -> "RegistrationPart":
        ret = cls(
            reg=reg,
            part=part,
            status=RegistrationPartStati(data["status"]),
            is_camping_mat=data["is_camping_mat"],
            lodgement=event.lodgements_by_id[data["lodgement_id"]] if data["lodgement_id"] else None,
        )
        if ret.lodgement is not None:
            ret.lodgement.parts_by_part[part].inhabitants.append(ret)
        return ret

    def __lt__(self, other: "RegistrationPart") -> bool:
        return (self.reg, self.part) < (other.reg, other.part)


@dataclasses.dataclass
class RegistrationTrack:
    reg: "Registration"
    track: "EventTrack"
    reg_part: "RegistrationPart"

    course: Course | None = None
    instructed_course: Course | None = None

    @property
    def is_potential_instructor(self) -> bool:
        return self.instructed_course is not None

    @property
    def is_instructor(self) -> bool:
        return self.instructed_course is not None and self.course == self.instructed_course

    @property
    def course_str(self) -> str:
        return (
            f"{self.course or '–'}"
            + " (instructor)" * self.is_instructor
            + f" ({self.reg_part.status})" * (self.reg_part.status != RegistrationPartStati.participant)
        )

    @property
    def attendee_str(self) -> str:
        if self.course is None:
            return "–"
        return (
            f"{self.reg.name}"
            + " (instructor)" * self.is_instructor
            + f" ({self.reg_part.status})" * (self.reg_part.status != RegistrationPartStati.participant)
        )

    @classmethod
    def from_json(cls, event: "Event", reg: Registration, track: "EventTrack", data: dict[str, Any]) -> "RegistrationTrack":
        ret = cls(
            track=track,
            reg=reg,
            reg_part=reg.parts_by_part[track.part],
            course=event.courses_by_id[int(data["course_id"])] if data["course_id"] else None,
            instructed_course=event.courses_by_id[int(data["course_instructor"])] if data["course_instructor"] else None,
        )

        if ret.course is not None and ret.track in ret.course.segments_by_track:
            ret.course.segments_by_track[ret.track].attendees.append(ret)
        if ret.instructed_course is not None and ret.track in ret.instructed_course.segments_by_track:
            instructed_segment = ret.instructed_course.segments_by_track[ret.track]
            instructed_segment.potential_instructors.append(ret)

        return ret

    def __lt__(self, other: "RegistrationTrack") -> bool:
        return (not self.is_instructor, self.reg, self.track) < (not self.is_instructor, other.reg, other.track)


class RegistrationPartStati(enum.Enum):
    """Spec for field status of event.registration_parts."""

    not_applied = -1  #:
    applied = 1  #:
    participant = 2  #:
    waitlist = 3  #:
    guest = 4  #:
    cancelled = 5  #:
    rejected = 6  #:

    @classmethod
    def involved_states(cls) -> tuple["RegistrationPartStati", ...]:
        return (
            RegistrationPartStati.applied,
            RegistrationPartStati.participant,
            RegistrationPartStati.waitlist,
            RegistrationPartStati.guest,
        )

    def is_involved(self) -> bool:
        """Any status which warrants further attention by the orgas."""
        return self in self.involved_states()

    def is_present(self) -> bool:
        """Any status which will be on site for the event."""
        return self in (RegistrationPartStati.participant, RegistrationPartStati.guest)

    def has_to_pay(self) -> bool:
        """Any status which should pay the participation fee."""
        return self in (RegistrationPartStati.applied, RegistrationPartStati.participant, RegistrationPartStati.waitlist)

    def __str__(self) -> str:
        return self.name

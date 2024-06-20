"""ITL reader module."""

import re
from pathlib import Path

from planetary_coverage.events import EventsDict, EventWindow

from ..misc import get_datetime
from ..misc.events import flatten, group

# ITL prefix pattern: # INST - KEY=VALUE ... or # INST - COMMENTS : VALUE
ATTRIBUTES = re.compile(r'^#\s+\w+\s+-\s+(?P<values>.*)')
COMMENTS = re.compile(r'^#\s+\w+\s+-\s+COMMENTS\s*:\s*(?P<value>.*)')
OBS_START = re.compile(r'(?P<inst>\w+)\s+OBS_START\s+(?P<key>\w*[a-zA-Z])(?:_\d+)?\s*')
OBS_END = re.compile(r'(?P<inst>\w+)\s+OBS_END\s+(?P<key>\w*[a-zA-Z])(?:_\d+)?$')


def read_itl(
    fname: str | Path,
    refs: dict | str | list | None = None,
    flat: bool = False,
) -> EventsDict | list:
    """Read ITL file.

    Note
    ----
    - The blocks can be prefixed with additional instrument parameters.

    - Blocks must be continuous, ie. consecutive OBS_START and OBS_END lines
      should have the same instrument observation name.
      If not an ValueError will be raised

    """
    lines = Path(fname).read_text().splitlines()

    events = _parse_itl(lines, refs=refs, filename=fname)

    return flatten(events) if flat else group(events)


def _parse_itl(
    lines: list[str],
    refs: dict | str | list | None = None,
    filename: str | Path | None = None,
) -> list[EventWindow]:
    """Parse ITL content as EventWindows list."""
    events = []
    attrs, header, comments, inst, key = {}, [], [], None, None

    for line in lines:
        if line.startswith('#'):
            header.append(line)

            if match := COMMENTS.match(line):
                comments.append(match.group('value').strip())
            elif match := ATTRIBUTES.match(line):
                attrs |= dict(
                    field.split('=', 1) for field in match.group('values').split(' ')
                )
            continue

        if match := OBS_START.search(line):
            start = get_datetime(line, refs=refs)
            inst = match.group('inst')
            key = match.group('key')

            attrs['PRIME'] = '(PRIME=TRUE)' in line
            continue

        if match := OBS_END.search(line):
            end = get_datetime(line, refs=refs)

            if inst != match.group('inst'):
                raise ValueError(
                    f"Instrument block mismatch: `{inst}` / `{match.group('inst')}`"
                )

            if key != match.group('key'):
                raise ValueError(
                    f"Obs name block mismatch: `{key}` / `{match.group('key')}`"
                )

            attrs['COMMENTS'] = ' / '.join(comments) if comments else None
            attrs['ITL'] = Path(filename) if filename else None

            event = EventWindow(key, t_start=start, t_end=end, INSTRUMENT=inst, **attrs)
            event.comments = header
            events.append(event)

        attrs, header, comments, inst, key = {}, [], [], None, None

    return events

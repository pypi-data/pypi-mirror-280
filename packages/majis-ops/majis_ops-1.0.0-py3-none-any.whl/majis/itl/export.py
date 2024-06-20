"""ITL export module."""

from pathlib import Path

from planetary_coverage.events import EventsDict, EventsList

from ..misc import fmt_datetime
from ..misc.csv import fmt_csv
from ..misc.events import concatenate
from ..misc.evf import ref_key
from .timeline import Timeline


def _save(fout: str | Path, content: list, suffix: str | None = None) -> Path:
    """Save content to file."""
    fout = Path(fout)

    if suffix and fout.suffix != suffix:
        raise ValueError(
            f'Output file name should ends with `{suffix}`: `{fout.name}` provided.'
        )

    fout.write_text('\n'.join(content))

    return fout


def save_itl(
    fout: str | Path | None,
    *events: EventsList | EventsDict,
    ref: str | None = None,
    header: str = None,
    overlap: bool = False,
) -> Path:
    """Save ITL events to a new ITL file.

    Note
    ----
    By default, ITL blocks must not overlap each other.
    This can be disable with `overlap=True`.

    """
    blocks = concatenate(*events, flat=True, overlap=overlap)

    content = [header] if header else []

    if ref:
        ref = ref_key(ref)

        content += [
            '# Relative time reference:',
            f'# {ref[1]}  {ref[0]}',
            '',
        ]

    for block in blocks:
        content.extend(block.comments)

        start, end = fmt_datetime(block.start, block.stop, ref=ref)

        inst = block['INSTRUMENT']
        prime = ' (PRIME=TRUE)' if block['PRIME'] else ''

        content.append(f'{start}  {inst}  OBS_START  {block.key}{prime}')
        content.append(f'{end}  {inst}  OBS_END    {block.key}')
        content.append('')  # empty line

    return _save(fout, content, suffix='.itl') if fout else content


def save_csv(
    fout: str | Path | None,
    *events: EventsList | EventsDict,
    ref: str | None = None,
    sep: str = ';',
    overlap: bool = False,
) -> Path:
    """Save ITL events to CSV.

    Note
    ----
    By default, ITL blocks must not overlap each other.
    This can be disable with `overlap=True`.

    """
    blocks = concatenate(*events, flat=True, overlap=overlap)

    content = fmt_csv(blocks, ref=ref, sep=sep)

    return _save(fout, content, suffix='.csv') if fout else content


def save_xlsm(
    fout: str | Path | None,
    *events: EventsList | EventsDict,
    timeline: str | Path | None = None,
    ca_ref: str | dict | None = None,
    overlap: bool = False,
) -> Path:
    """Save ITL events to XLSM timeline.

    If a timeline is provided but no explicit output file
    the output file will be same in the original timeline.

    """
    blocks = concatenate(*events, flat=True, overlap=overlap)

    timeline = Timeline(blocks, timeline=timeline, ca_ref=ca_ref)

    return timeline.save(fout)

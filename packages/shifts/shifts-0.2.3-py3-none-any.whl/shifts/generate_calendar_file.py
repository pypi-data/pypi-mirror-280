import calendar
import os
from datetime import date, datetime
from typing import List, Tuple
from zoneinfo import ZoneInfo

import typer
from dateutil.relativedelta import relativedelta
from ics import Calendar, Event

from shifts.shift import Shift

timezone = ZoneInfo("Europe/Lisbon")


def generate_calendar_file(shifts):
    c = Calendar()

    year, month = next_year_month()
    try:
        clean_shifts = validate_shifts(shifts, year, month)
    except ValueError as e:
        typer.echo(f"Invalid shifts found, {str(e)}", err=True)
        raise typer.Exit(code=1)

    for day, shift in enumerate(clean_shifts, start=1):
        if shift == "D":
            continue

        if shift == "F":
            s = Shift(shift, year, month, day)
            event = Event(
                name=s.name,
                begin=date(year, s.begin_month, s.begin_day),  # type: ignore
            )
            event.make_all_day()
            c.events.add(event)
            continue

        if shift == "LF":
            s = Shift("F", year, month, day)
            event = Event(
                name=s.name,
                begin=date(year, s.begin_month, s.begin_day),  # type: ignore
            )
            event.make_all_day()
            c.events.add(event)
            continue

        if shift == "MN" or shift == "MT" or shift == "TN":
            for name in shift:
                s = Shift(name, year, month, day)
                c.events.add(
                    Event(
                        name=s.name,
                        begin=datetime(
                            year,
                            s.begin_month,
                            s.begin_day,
                            s.begin_hour,
                            s.begin_minute,
                            0,
                            tzinfo=timezone,
                        ),
                        end=datetime(
                            year, s.end_month, s.end_day, s.end_hour, s.end_minute, 0
                        ),
                    )
                )

            continue

        s = Shift(shift, year, month, day)
        c.events.add(
            Event(
                name=s.name,
                begin=datetime(
                    year,
                    s.begin_month,
                    s.begin_day,
                    s.begin_hour,
                    s.begin_minute,
                    0,
                    tzinfo=timezone,
                ),
                end=datetime(
                    year,
                    s.end_month,
                    s.end_day,
                    s.end_hour,
                    s.end_minute,
                    0,
                    tzinfo=timezone,
                ),
            )
        )

    schedule_file = os.getenv("SCHEDULE_FILE")
    if not schedule_file:
        schedule_file = f"schedule_{year}_{month}.ics"

    with open(schedule_file, "w") as my_file:
        my_file.writelines(c.serialize_iter())

    print(f"Calendar file '{schedule_file}' created successfully.")


def next_year_month() -> Tuple[int, int]:
    now = datetime.now(timezone)
    next_month = now + relativedelta(months=1)
    return next_month.year, next_month.month


def validate_shifts(shifts, year, month) -> List[str]:
    """
    Receives a string with the shifts and validates those, and transforms into
     a list of shifts.

    :param shifts: The string with of shifts to validate
    :param year: The year the shifts will be in
    :param month: The month the shifts will be in
    :return: A list of shifts
    """

    if " " not in shifts or not shifts.count(" ") > 10:
        raise ValueError(f"'{shifts}' is not a valid option")

    _, number_of_days = calendar.monthrange(year, month)
    shifts = shifts.strip().split(" ")
    shifts = [item.upper() for item in shifts]
    if len(shifts) != number_of_days:
        raise ValueError(f"expected {number_of_days} shifts, but got {len(shifts)}")

    return shifts

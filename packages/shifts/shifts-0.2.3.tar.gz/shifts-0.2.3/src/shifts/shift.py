from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

timezone = ZoneInfo("Europe/Lisbon")


class Shift:
    def __init__(self, shift_symbol, year, month, day):
        self._shift_symbol = shift_symbol.upper()

        self._shift_names = {
            "M": "Manhã",
            "T": "Tarde",
            "N": "Noite",
            "F": "Folga",
        }

        self._validate_shift_name()

        start_hour = {
            "M": 8,
            "T": 14,
            "N": 21,
            "F": 0,
        }
        start_minute = {
            "M": 0,
            "T": 30,
            "N": 0,
            "F": 0,
        }
        delta_end_hour = {
            "M": 7,
            "T": 7,
            "N": 11,
            "F": 24,
        }
        delta_end_minute = {
            "M": 0,
            "T": 0,
            "N": 30,
            "F": 0,
        }

        self._start = datetime(
            year,
            month,
            day,
            start_hour[self._shift_symbol],
            start_minute[self._shift_symbol],
            tzinfo=timezone,
        )
        self._end = self._start + timedelta(
            hours=delta_end_hour[self._shift_symbol],
            minutes=delta_end_minute[self._shift_symbol],
        )

    def _validate_shift_name(self):
        try:
            self._shift_names[self._shift_symbol]
        except KeyError:
            raise ValueError(f"Invalid shift symbol'{self._shift_symbol}'")

    @property
    def name(self) -> str:
        return self._shift_names[self._shift_symbol]

    @property
    def begin_month(self) -> int:
        return self._start.month

    @property
    def begin_day(self) -> int:
        return self._start.day

    @property
    def begin_hour(self) -> int:
        return self._start.hour

    @property
    def begin_minute(self) -> int:
        return self._start.minute

    @property
    def end_month(self) -> int:
        return self._end.month

    @property
    def end_day(self) -> int:
        return self._end.day

    @property
    def end_hour(self) -> int:
        return self._end.hour

    @property
    def end_minute(self) -> int:
        return self._end.minute

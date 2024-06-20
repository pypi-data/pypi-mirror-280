import typer
from typing_extensions import Annotated

from shifts.generate_calendar_file import generate_calendar_file

help_msg: str = "Create an ical file with the shifts for the next month"
app = typer.Typer(add_completion=False, help=help_msg)


@app.command(options_metavar="")
def shifts_(
    shifts: Annotated[
        str,
        typer.Argument(
            show_default=False,
            metavar='"F T N D F M M T N D F M M"',
            help="For each day, choose a symbol that represents the shift",
        ),
    ]
):
    """
    Symbols:\n
    M: Morning\n
    T: Afternoon\n
    N: Night\n
    D: Rest Day\n
    F: Day off\n
    LF: Vacations\n
    MN: Morning and Night\n
    MT: Morning and Afternoon
    TN: Afternoon and Night
    """

    generate_calendar_file(shifts)

import typing
from .strip import Strip

class StripSection(typing.NamedTuple):
    strip: Strip
    top: float
    bottom: float

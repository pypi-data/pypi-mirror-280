import numpy as np
import numpy.typing as npt
from collections.abc import Iterable

from .strip import Strip

def _squish(diagram: np.ndarray, *, scale: float) -> npt.ArrayLike:
    return np.arctan(scale * diagram)

_default_strip = Strip()

def unravel_graded(graded: Iterable[np.ndarray],
                   /,
                   scale: float = 1.0) -> npt.ArrayLike:

    squished_graded = (
        _squish(component, scale=scale) for component in graded
    )

    return _default_strip.unravel_squished_graded(squished_graded)

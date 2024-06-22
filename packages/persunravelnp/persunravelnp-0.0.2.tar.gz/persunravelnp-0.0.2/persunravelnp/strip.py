from typing import Tuple, NamedTuple
import itertools as it
from enum import StrEnum
from collections.abc import Iterable, Sequence
import numpy as np
import numpy.typing as npt

_unit_matrix = np.array(
    [[1, 0],
     [0, 1]]
)

_reflect01 = np.array(
    [[-1, 0],
     [ 0, 1]]
)

_reflect02 = np.array(
    [[0, 1],
     [1, 0]]
)

class Orientation(StrEnum):
    ORDINARY = 'ordinary'
    CROSS = 'cross'

def _box_product(a: np.ndarray,
                 b: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    intermediate_shape = (a.shape[-2], b.shape[-2], 2)
    total_size = a.shape[-2] * b.shape[-2]
    an = np.expand_dims(a, -2)
    bn = np.expand_dims(b, -3)
    ann = np.broadcast_to(an, an.shape[:-3] + intermediate_shape)
    bnn = np.broadcast_to(bn, bn.shape[:-3] + intermediate_shape)
    return (
        ann.reshape( an.shape[:-3] + (total_size, 2) ),
        bnn.reshape( bn.shape[:-3] + (total_size, 2) )
    )

class Strip(NamedTuple):
    root_l0: float = 0
    root_l1: float = -np.pi / 2.0
    orientation: Orientation = Orientation.ORDINARY

    def _maybe_flip(self, dgm: np.ndarray) -> np.ndarray:
        if self.orientation is Orientation.ORDINARY:
            return dgm
        else:
            return dgm @ _reflect01

    @property
    def _ord_root_l0(self):
        if self.orientation is Orientation.ORDINARY:
            return self.root_l0
        else:
            return -self.root_l0
        
    @property    
    def _ord_root_l1(self):
        if self.orientation is Orientation.ORDINARY:
            return self.root_l1
        else:
            return -self.root_l1
        
    def kernel(self,
               dgm01: np.ndarray,
               dgm02: np.ndarray,
               /) -> npt.ArrayLike:
        dgm01r, dgm02r = _box_product( self._maybe_flip(dgm01),
                                       self._maybe_flip(dgm02)
                                      )
        join = np.maximum(dgm01r, dgm02r)
        meet = np.minimum(dgm01r, dgm02r)
        area = np.squeeze(
            np.maximum( meet.take([1], axis=-1) -
                        join.take([0], axis=-1) +
                        self._ord_root_l0,
                        0
                       ) *
            np.maximum( meet.take([0], axis=-1) -
                        join.take([1], axis=-1) -
                        self._ord_root_l1,
                        0
                       ),
            axis=-1
        )
        return np.sum(area, -1)

    def gram(self,
             dgms01: npt.ArrayLike,
             dgms02: npt.ArrayLike,
             /) -> npt.ArrayLike:
        return self.kernel( np.expand_dims(dgms01, -3),
                            np.expand_dims(dgms02, -4)
                           )
    
    def unravel_squished_graded(self,
                                graded: Iterable[np.ndarray],
                                /) -> npt.ArrayLike:

        reflection_powers = it.cycle((_unit_matrix, _reflect02))
        offsets = np.array( [[ self._ord_root_l1, -self._ord_root_l0],
                             [-self._ord_root_l0,  self._ord_root_l1]] )
        offset_multipliers = it.accumulate(
            it.cycle( [np.array([1, 0]), np.array([0, 1])] ),
            initial=np.array([0, 0])
        )

        return self._maybe_flip(
            np.concatenate(
                [ self._maybe_flip(diagram) @ reflection_power +
                  offset_multiplier @ offsets
                  for
                  diagram,  reflection_power,  offset_multiplier in
                  zip(graded, reflection_powers, offset_multipliers)
                 ]
            )
        )

    def pad_unravelled_diagrams(self,
                                dgms: Sequence[np.ndarray],
                                /) -> npt.ArrayLike:
        max_length = max([dgm.shape[0] for dgm in dgms])
        return np.stack(
            [ np.append( dgm,
                         np.full((max_length - dgm.shape[0], 2),
                                 [self.root_l0, 0]
                                 ),
                         axis=0
                        )
              # np.pad( dgm,
              #       [(0, max_length - dgm.shape[0]), (0, 0)] )
              for dgm in dgms
             ]
        )

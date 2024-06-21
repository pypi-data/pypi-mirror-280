import numpy as np
from collections.abc import Iterable

def _box_product(a: np.array, b: np.array) -> (np.array, np.array):
    intermediate_shape = (a.shape[0], b.shape[0], 2)
    total_size = a.shape[0] * b.shape[0]
    an = np.expand_dims(a, 1)
    bn = np.expand_dims(b, 0)
    ann = np.broadcast_to(an, intermediate_shape)
    bnn = np.broadcast_to(bn, intermediate_shape)
    return (
        ann.reshape((total_size, 2)),
        bnn.reshape((total_size, 2))
    )

def kernel(dgm01: np.array,
           dgm02: np.array,
           /,
           *,
           root_l0: float = 0,
           root_l1: float = np.pi / 2) -> float:
    dgm01r, dgm02r = _box_product(dgm01, dgm02)
    join_x = np.minimum(dgm01r[:,0], dgm02r[:,0])
    join_y = np.minimum(dgm01r[:,1], dgm02r[:,1])
    meet_x = np.maximum(dgm01r[:,0], dgm02r[:,0])
    meet_y = np.maximum(dgm01r[:,1], dgm02r[:,1])
    area = (
        np.maximum(join_y - meet_x + root_l1, 0) *
        np.maximum(join_x - meet_y - root_l0, 0)
    )
    return np.sum(area)

def mk_gram_mat(dgms01: Iterable[np.array],
                dgms02: Iterable[np.array],
                /,
                *,
                root_l0: float = 0,
                root_l1: float = np.pi / 2) -> np.array:
    return np.array([[kernel(dgm01,
                             dgm02,
                             root_l0=root_l0,
                             root_l1=root_l1)
                      for dgm02 in dgms02]
                     for dgm01 in dgms01]
                    )

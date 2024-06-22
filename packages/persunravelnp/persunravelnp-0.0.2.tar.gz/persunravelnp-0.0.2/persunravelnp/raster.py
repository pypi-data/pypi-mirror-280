from math import ceil
import numpy as np

class Raster:
    __slots__ = ('_strip_width',
                 '_sidelen',
                 '_pixel_area',
                 '_padding',
                 '_px',
                 '_py'
                 )

    def __init__(self,
                 /,
                 ambient_dim: int,
                 pixel_density: int,
                 strip_width: float = np.pi/2.0,
                 padding: int = 0
                 ):
        self._strip_width = strip_width
        self._sidelen = self._strip_width / pixel_density
        self._pixel_area = self._sidelen * self._sidelen
        self._padding = padding

        self._px = np.arange(
            start = (
                -ceil((ambient_dim-1)/2.0) * self._strip_width -
                self._padding * self._sidelen
            ),
            stop = self._strip_width + self._padding * self._sidelen,
            step = self._sidelen
        )[np.newaxis, :, np.newaxis]

        self._py = np.flip(
            np.arange(
                start = (
                    -ceil(ambient_dim/2.0 - 1.0) * self._strip_width -
                    self._padding * self._sidelen
                ),
                stop = self._strip_width + self._padding * self._sidelen,
                step = self._sidelen
            )
        )[:, np.newaxis, np.newaxis]

    @property
    def sidelen(self):
        return self._sidelen
        
    @property
    def pixel_area(self):
        return self._pixel_area
        
    def rasterize(self, dgm: np.ndarray) -> np.ndarray:
        dgm_emb = np.expand_dims( dgm, axis = (-3, -4) )
        x = np.squeeze( dgm_emb.take([0], axis=-1), axis = -1 )
        y = np.squeeze( dgm_emb.take([1], axis=-1), axis = -1 )

        hor_seg = np.maximum(
            np.minimum(
                np.minimum(
                    self._px + self._sidelen - x,
                    y - self._px
                ),
                self._sidelen
            ),
            0
        )

        vert_seg = np.maximum(
            np.minimum(
                np.minimum(
                    self._py + self._sidelen - y,
                    x - self._py + self._strip_width
                ),
                self._sidelen
            ),
            0
        )

        return np.squeeze(
            np.expand_dims(hor_seg , axis=-2) @
            np.expand_dims(vert_seg, axis=-1),
            axis=(-2, -1)
        ) / self._pixel_area

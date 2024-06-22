from typing import ClassVar, Optional
from dataclasses import dataclass
import io
import numpy as np
import numpy.typing as npt
from collections.abc import Iterable
import importlib

from .sizes import (
    Unit,
    Length,
    Sizes
)

from .viewbox import Viewbox

from ._static_assets import (
    _point_cloud_background,
    _stylesheet,
    _markers
)

from ._jinja_templates import (
    _standalone_template,
    _dependent_template,
    _style_n_defs_template
)

_reflect = np.array(
    [[1,  0],
     [0, -1]]
)

class SVG(str):
    def _repr_svg_(self):
        return self
    def _repr_html_(self):
        return self

@dataclass(kw_only=True, slots=True)
class Frame:
    sizes: Sizes = Sizes(height = Length(700.0, Unit.PX))
    padding: float = 0.1
    viewbox: Optional[Viewbox] = None
    background: str = _point_cloud_background
    stylesheet: ClassVar[str] = _stylesheet
    defs: ClassVar[str] = _markers
    standalone: ClassVar[bool] = True

    @classmethod
    def complement_notebook(cls):
        # TODO: Catch ModuleNotFound and raise a more informative exception
        #       saying that this method is only intended to be called
        #       from Jupyter Notebook
        ipython_display_mod = importlib.import_module('IPython.display')
        ipython_display_mod.display(
            ipython_display_mod.HTML(
                _style_n_defs_template.render(
                    stylesheet=cls.stylesheet,
                    defs=cls.defs
                )                
            )
        )
        # Apparently triggering this
        # as in https://stackoverflow.com/questions/21664940/force-browser-to-trigger-reflow-while-changing-css
        # is not enough
        # ipython_display_mod.display(
        #     ipython_display_mod.Javascript('console.log(element.offsetHeight)')
        # )
        cls.standalone = False

    def draw(self,
             dgms: Iterable[npt.ArrayLike],
             /,
             *,
             sizes: Optional[Sizes] = None,
             padding: Optional[float] = None,
             viewbox: Optional[Viewbox] = None,
             standalone: Optional[bool] = None
             ) -> SVG:

        if sizes is None:
            sizes = self.sizes
            
        if padding is None:
            padding = self.padding

        if viewbox is None:
            viewbox = self.viewbox
            
        if standalone is None:
            standalone = self.standalone
            
        str_dgms: list[str] = []
        min_x = 0.0
        min_y = 0.0
        max_x = 0.0
        max_y = 0.0

        for dgm in dgms:
            transformed_dgm = dgm @ _reflect
            if viewbox is None:
                dgm_min_x, dgm_min_y = np.min(transformed_dgm, axis=0)
                dgm_max_x, dgm_max_y = np.max(transformed_dgm, axis=0)
                min_x = min(min_x, dgm_min_x)
                min_y = min(min_y, dgm_min_y)
                max_x = max(max_x, dgm_max_x)
                max_y = max(max_y, dgm_max_y)
            with io.StringIO() as txt_stream:
                np.savetxt(txt_stream,
                           transformed_dgm,
                           fmt='%.5f',
                           delimiter=',',
                           newline=' '
                           )
                str_dgms.append(txt_stream.getvalue())

        if viewbox is None:
            min_x -= padding
            min_y -= padding
            max_x += padding
            max_y += padding
        else:
            min_x =  viewbox.left
            min_y = -viewbox.top
            max_x =  viewbox.right
            max_y = -viewbox.bottom
    
        vb_width = max_x - min_x
        vb_height = max_y - min_y
            
        if standalone:
            return SVG(
                _standalone_template.render(
                    str_dgms=str_dgms,
                    min_x=min_x, min_y=min_y,
                    vb_width=vb_width, vb_height=vb_height,
                    sizes=sizes,
                    stylesheet=self.stylesheet,
                    defs=self.defs,
                    background=self.background
                )                
            )
        else:
            return SVG(
                _dependent_template.render(
                    str_dgms=str_dgms,
                    min_x=min_x, min_y=min_y,
                    vb_width=vb_width, vb_height=vb_height,
                    sizes=sizes,
                    background=self.background
                )
            )

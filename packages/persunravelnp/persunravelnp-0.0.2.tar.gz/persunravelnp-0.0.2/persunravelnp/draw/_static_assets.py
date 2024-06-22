# https://stackoverflow.com/a/20885799
from importlib import resources as impresources
from . import templates

_point_cloud_strip_background_file = (
    impresources.files(templates) / 'point-cloud-strip-background.svg'
)

with _point_cloud_strip_background_file.open("rt") as f:
    _point_cloud_background = f.read()

_stylesheet_file = impresources.files(templates) / 'unravelled-diagrams.css'

with _stylesheet_file.open("rt") as f:
    _stylesheet = f.read()

_markers_file = impresources.files(templates) / 'markers.svg'

with _markers_file.open("rt") as f:
    _markers = f.read()

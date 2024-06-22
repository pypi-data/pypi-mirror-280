from jinja2 import Environment, PackageLoader

_env = Environment(
    loader=PackageLoader("persunravelnp.draw"),
    autoescape=False
)

_standalone_template = _env.get_template(
    "unravelled-diagrams-standalone.svg"
)

_dependent_template = _env.get_template(
    "unravelled-diagrams-dependent.svg"
)

_style_n_defs_template = _env.get_template(
    "style-n-defs.html"
)

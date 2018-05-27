import pathlib

from hydra.views import index
from hydra.views import node_detail

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get("/", index)
    app.router.add_get("/node/{node_id}", node_detail, name="node_detail")
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static("/static/", path=PROJECT_ROOT / "static", name="static")

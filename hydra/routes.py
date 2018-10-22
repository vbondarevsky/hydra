import pathlib

from hydra.handler.node import NodeHandler

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.add_routes(NodeHandler().routes)
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static("/", path=PROJECT_ROOT / "static", name="static")

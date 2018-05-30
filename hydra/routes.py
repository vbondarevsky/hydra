import pathlib

from hydra.views import index
from hydra.views import node_detail


PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get("/", index)
    app.router.add_get("/node/{node_id}", node_detail, name="node_detail")
    app.router.add_get("/node/add", node_detail, name="node_add")
    setup_static_routes(app)


def setup_static_routes(app):
    # TODO: app.router.add_static("/static/", path=PROJECT_ROOT / "static", name="static")
    pass

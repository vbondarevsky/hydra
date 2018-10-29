import os.path
import pathlib

import aiohttp

from hydra.handler import ClusterHandler
from hydra.handler import NodeHandler

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get("/", root_handle)
    app.add_routes(NodeHandler().routes)
    app.add_routes(ClusterHandler().routes)
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static("/", path=os.path.join(PROJECT_ROOT, "static"), name="static")


async def root_handle(request):
    return aiohttp.web.FileResponse(os.path.join(PROJECT_ROOT, "static", "index.html"))

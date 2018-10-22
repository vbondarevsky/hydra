import aiohttp.web

from hydra.routes import setup_routes
from hydra.settings import settings


def run_server():
    app = aiohttp.web.Application(debug=settings["debug"])
    app["settings"] = settings
    setup_routes(app)
    aiohttp.web.run_app(app, host=settings["host"], port=settings["port"])


if __name__ == "__main__":
    run_server()

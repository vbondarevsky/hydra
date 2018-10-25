import aiohttp.web

from hydra.db.connect import close_db
from hydra.db.connect import open_db
from hydra.routes import setup_routes
from hydra.settings import settings


def run_server():
    app = aiohttp.web.Application(debug=settings["debug"])
    app["settings"] = settings
    setup_routes(app)

    app.on_startup.append(open_db)
    app.on_cleanup.append(close_db)

    aiohttp.web.run_app(app, host=settings["host"], port=settings["port"])


if __name__ == "__main__":
    run_server()

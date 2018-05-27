import aiohttp.web
import aiohttp_jinja2
import jinja2

from hydra.routes import setup_routes
from hydra.settings import config

app = aiohttp.web.Application(debug=config["debug"])

aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader("hydra", "templates"))

setup_routes(app)
app["config"] = config
aiohttp.web.run_app(app, host=config["host"], port=config["port"])

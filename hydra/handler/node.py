import aiohttp.web

from hydra.db.models import Node
from hydra.handler.base_handler import BaseHandler


class NodeHandler(BaseHandler):

    @property
    def routes(self):
        return [
            aiohttp.web.post(self.build_route("/nodes"), self.create),
            aiohttp.web.get(self.build_route("/nodes"), self.read),
            aiohttp.web.get(self.build_route("/nodes/{node_id}"), self.read),
            aiohttp.web.put(self.build_route("/nodes/{node_id}"), self.update),
            aiohttp.web.delete(self.build_route("/nodes/{node_id}"), self.delete),
            aiohttp.web.get(self.build_route("/nodes/{node_id}/status"), self.get_status),
        ]

    async def create(self, request):
        return aiohttp.web.json_response(Node.add(request.app["db"], await request.json()), status=201)

    async def read(self, request):
        return aiohttp.web.json_response(Node.read(request.app["db"], request.match_info.get("node_id", None)))

    async def update(self, request):
        pass

    async def delete(self, request):
        Node.remove(request.app["db"], request.match_info.get("node_id", None))
        return aiohttp.web.json_response(status=204)

    async def get_status(self, request):
        async with aiohttp.ClientSession() as session:
            node_id = request.match_info.get('node_id', None)
            url = request.app["db"].query(Node).filter_by(id=node_id).first().url
            async with session.get(f"{url}/api/v1/heartbeat", verify_ssl=False) as resp:
                return aiohttp.web.json_response(await resp.json())

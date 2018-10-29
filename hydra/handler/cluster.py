import aiohttp.web

from hydra.db.models import Node
from hydra.handler.base_handler import BaseHandler


class ClusterHandler(BaseHandler):

    @property
    def routes(self):
        return [
            aiohttp.web.post(self.build_route("/nodes/{node_id}/clusters"), self.create),
            aiohttp.web.get(self.build_route("/nodes/{node_id}/clusters"), self.read),
            aiohttp.web.get(self.build_route("/nodes/{node_id}/clusters/{cluster_id}"), self.read),
            aiohttp.web.put(self.build_route("/nodes/{node_id}/clusters/{cluster_id}"), self.update),
            aiohttp.web.delete(self.build_route("/nodes/{node_id}/clusters/{cluster_id}"), self.delete),
        ]

    async def create(self, request):
        pass

    async def read(self, request):
        node_id = request.match_info.get("node_id")
        url = Node.read(request.app["db"], node_id)["url"]
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{url}/api/v1/clusters", verify_ssl=False) as resp:
                return aiohttp.web.json_response(await resp.json())

    async def update(self, request):
        pass

    async def delete(self, request):
        pass

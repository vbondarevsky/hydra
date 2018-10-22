import aiohttp.web

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
        ]

    async def create(self, request):
        pass

    async def read(self, request):
        node_id = request.match_info.get('node_id', None)
        data = get_node(node_id)
        return aiohttp.web.json_response(data)

    async def update(self, request):
        pass

    async def delete(self, request):
        pass


def get_node(node_id):
    if node_id:
        return {"id": 1, "name": "test_node", "host": "localhost", "port": 8080}
    else:
        return [{"id": 1, "name": "test_node", "host": "localhost", "port": 8080}]

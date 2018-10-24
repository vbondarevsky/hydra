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
            # TODO: временно или нет?
            aiohttp.web.view(self.build_route("/nodes/{node_id}"), self.options),
        ]

    async def create(self, request):
        pass

    async def read(self, request):
        node_id = request.match_info.get('node_id', None)
        data = get_node(node_id)
        # TODO: Заголовок нужен, чтобы разрабатывать можно было, запуская фронт и бек на разных портах
        return aiohttp.web.json_response(data, headers={'Access-Control-Allow-Origin': '*'})

    async def update(self, request):
        pass

    async def delete(self, request):
        return aiohttp.web.json_response({}, headers={'Access-Control-Allow-Origin': '*'})

    async def options(self, request):
        return aiohttp.web.json_response({}, headers={'Access-Control-Allow-Origin': '*',
                                                      'Access-Control-Allow-Methods': '*'})


def get_node(node_id):
    if node_id:
        return {"id": 1, "name": "test_node", "host": "localhost", "port": 8080}
    else:
        return [
            {"id": 1, "name": "test_node", "host": "localhost", "port": 8080},
            {"id": 2, "name": "test_node", "host": "localhost", "port": 8080},
            {"id": 3, "name": "test_node", "host": "localhost", "port": 8080},
            {"id": 4, "name": "test_node", "host": "localhost", "port": 8080},
            {"id": 5, "name": "test_node", "host": "localhost", "port": 8080},
        ]

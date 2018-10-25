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

            # TODO: временно или нет?
            aiohttp.web.options(self.build_route("/nodes/{node_id}"), self.options),
            aiohttp.web.options(self.build_route("/nodes"), self.options),
            aiohttp.web.options(self.build_route("/nodes/{node_id}/status"), self.options),

        ]

    async def create(self, request):
        node = await request.json()

        new_node = Node(**node, user="", password="")
        request.app["db"].add(new_node)
        request.app["db"].commit()
        return aiohttp.web.json_response({"id": new_node.id, "name": new_node.name, "url": new_node.url},
                                         headers={'Access-Control-Allow-Origin': '*'},
                                         status=201)

    async def read(self, request):
        node_id = request.match_info.get('node_id', None)
        data = get_node(request.app["db"], node_id)
        # TODO: Заголовок нужен, чтобы разрабатывать можно было, запуская фронт и бек на разных портах
        return aiohttp.web.json_response(data, headers={'Access-Control-Allow-Origin': '*'})

    async def update(self, request):
        pass

    async def delete(self, request):
        return aiohttp.web.json_response({}, headers={'Access-Control-Allow-Origin': '*'})

    async def get_status(self, request):
        async with aiohttp.ClientSession() as session:
            node_id = request.match_info.get('node_id', None)
            url = request.app["db"].query(Node).filter_by(id=node_id).first().url
            async with session.get(f"{url}/api/v1/heartbeat", verify_ssl=False) as resp:
                return aiohttp.web.json_response(await resp.json(), headers={'Access-Control-Allow-Origin': '*'})

    async def options(self, request):
        return aiohttp.web.json_response({}, headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers",
        })


def get_node(db_session, node_id):
    if node_id:
        node = db_session.query(Node).filter_by(id=node_id).first()
        return {"id": node.id, "name": node.name, "url": node.url}
    else:
        nodes = db_session.query(Node).all()
        result = []
        for node in nodes:
            result.append({"id": node.id, "name": node.name, "url": node.url})
        return result

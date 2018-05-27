import aiohttp_jinja2


@aiohttp_jinja2.template("nodes.html")
async def index(request):
    nodes = [
        {
            "id": 1,
            "name": "dev",
            "url": "http://localhost:9090",
        },
        {
            "id": 2,
            "name": "dev2",
            "url": "http://localhost:8090",
        },
        {
            "id": 3,
            "name": "dev3",
            "url": "http://localhost:8080",
        },
    ]
    return {"nodes": nodes}


@aiohttp_jinja2.template("node_detail.html")
async def node_detail(request):
    node = {
        "name": "dev",
        "url": "http://localhost:9090",
        "clusters": [
            {"name": "loc:1541", "infobases": [{"name": "acc"}, {"name": "hrm"}]},
        ],
    }
    return node

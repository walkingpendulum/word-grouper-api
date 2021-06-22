from aiohttp import web


async def ping(request: web.Request):
    return web.Response(text="pong")


async def get_words(request: web.Request):
    return web.json_response(data={})


async def put_word(request: web.Request):
    return web.json_response(data={})


async def delete_word(request: web.Request):
    return web.json_response(data={})

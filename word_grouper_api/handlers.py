import json

from aiohttp import web

from word_grouper_api import state


async def ping(request: web.Request):
    return web.Response(text="pong")


async def get_words(request: web.Request):
    words_ = state.get_words(request.app)
    words = {folder: list(sorted(words_[folder])) for folder in words_}

    return web.Response(text=f"{json.dumps(words, indent=4)}\n", content_type="application/json")


async def put_word(request: web.Request):
    word = request.match_info["word"]
    payload = await request.json()
    if "folder" not in payload:
        return web.Response(status=400, reason="Validation Error: folder is absent")

    folder = payload["folder"]
    if not isinstance(folder, str):
        return web.Response(status=400, reason="Validation Error: folder should be a string")

    state.add_word(word=word, folder=folder, app=request.app)
    return web.Response(status=204)


async def delete_word(request: web.Request):
    word = request.match_info["word"]
    state.remove_word(word=word, app=request.app)
    return web.Response(status=204)

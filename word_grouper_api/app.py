from aiohttp import web

from word_grouper_api import handlers


def make_app() -> web.Application:
    app = web.Application()
    app.add_routes([
        web.get('/ping', handlers.ping),
        web.get('/api/v1/words', handlers.get_words),
    ])

    return app

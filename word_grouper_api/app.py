from aiohttp import web

from word_grouper_api import handlers
from word_grouper_api.state import setup_state


def make_app() -> web.Application:
    app = web.Application()

    setup_state(app)
    app.add_routes([
        web.get('/ping', handlers.ping),
        web.get('/api/v1/words', handlers.get_words),
        web.put('/api/v1/words/{word}', handlers.put_word),
        web.delete('/api/v1/words/{word}', handlers.delete_word),
    ])

    return app

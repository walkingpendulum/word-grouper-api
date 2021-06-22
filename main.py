from aiohttp import web

from word_grouper_api.app import make_app
from word_grouper_api.logs import setup_logging


if __name__ == '__main__':
    setup_logging()
    web.run_app(make_app())

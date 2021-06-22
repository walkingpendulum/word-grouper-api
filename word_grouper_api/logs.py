import logging


def setup_logging():
    logging.basicConfig()
    logging.getLogger("aiohttp").setLevel(logging.INFO)

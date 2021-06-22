from collections import defaultdict

from aiohttp import web

FOLDER_TO_WORDS = "folder_to_words"
WORDS_TO_FOLDER = "word_to_folder"


def setup_state(app: web.Application) -> None:
    app[WORDS_TO_FOLDER] = {}
    app[FOLDER_TO_WORDS] = defaultdict(set)


def add_word(word: str, folder: str, app: web.Application) -> None:
    app[WORDS_TO_FOLDER][word] = folder
    app[FOLDER_TO_WORDS][folder].add(word)


def remove_word(word: str, app: web.Application) -> None:
    folder = app[WORDS_TO_FOLDER].pop(word, None)
    if folder:
        app[FOLDER_TO_WORDS][folder].discard(word)
        if not app[FOLDER_TO_WORDS][folder]:
            del app[FOLDER_TO_WORDS][folder]


def get_words(app: web.Application) -> dict:
    return app[FOLDER_TO_WORDS]

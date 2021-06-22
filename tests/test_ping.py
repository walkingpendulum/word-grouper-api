from word_grouper_api.app import make_app


async def test_ping(aiohttp_client, loop):
    app = make_app()
    client = await aiohttp_client(app)
    resp = await client.get('/ping')
    assert resp.status == 200
    text = await resp.text()
    assert 'pong' == text

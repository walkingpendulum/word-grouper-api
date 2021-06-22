from word_grouper_api.app import make_app


async def test_create_read_delete(aiohttp_client, loop):
    app = make_app()
    client = await aiohttp_client(app)

    resp = await client.get('/api/v1/words')
    assert resp.status == 200
    data = await resp.json()
    assert {} == data

    resp = await client.put('/api/v1/words/this_is_a_word')
    assert resp.status == 200

    resp = await client.delete('/api/v1/words/this_is_a_word')
    assert resp.status == 200


import pprint
from publisher.methods import Publisher


async def ping_pong(request: dict):
    pprint.pprint(request)
    return 1


async def send_message__internal_messager(request: dict):
    publisher = await Publisher.create()
    return await publisher.send_message__internal_messager(request["ping"])
    

async def call_upper_word__internal_messager(request: dict):
    publisher = await Publisher.create()
    return await publisher.call_upper_word__internal_messager(request["ping"])

async def send_message__internal_messager_new(request: dict):
    publisher = await Publisher.create()
    return await publisher.send_message__internal_messager_new(request["ping"])


async def call_upper_word_by_jsonrpc__internal_messager(request: dict):
    publisher = await Publisher.create()
    return await publisher.call_upper_word_by_jsonrpc__internal_messager(request["ping"])

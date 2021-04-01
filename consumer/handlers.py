from consumer import methods
from consumer import schema
from consumer.helpers import validate_request_schema

# without validate
async def simple_message(message):
    print("Message body is: %r" % message.body)
    await message.channel.basic_ack(message.delivery.delivery_tag)



@validate_request_schema(schema.DefaultRequest)
async def ping_pong(request: dict):
    response = await methods.test_hello_world(request)
    return response


@validate_request_schema(schema.DefaultRequest)
async def send_message__internal_messager(request: dict):
    response = await methods.send_message__internal_messager(request)
    return response

@validate_request_schema(schema.DefaultRequest)
async def send_message__internal_messager_new(request: str):
    response = await methods.send_message__internal_messager_new(request)
    return response



@validate_request_schema(schema.DefaultRequest)
async def call_upper_word__internal_messager(request: dict):
    response = await methods.call_upper_word__internal_messager(request)
    return response


@validate_request_schema(schema.DefaultRequest)
async def call_upper_word_by_jsonrpc__internal_messager(request: dict):
    response = await methods.call_upper_word_by_jsonrpc__internal_messager(request)
    return response

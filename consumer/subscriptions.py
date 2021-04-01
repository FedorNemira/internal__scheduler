import aiormq
from termcolor import cprint

from consumer import handlers
from settings import AMQP_URI


async def consumer_subscriptions():

    connection = await aiormq.connect(AMQP_URI)
    channel = await connection.channel()
    cprint("AMQP:     ready [yes]", "green")

    # declare queues
    simple_message__declared = await channel.queue_declare("reminder24:internal__scheduler:simple_message")
    ping_pong__declared = await channel.queue_declare("reminder24:internal__scheduler:test_hello_world")

    # bind handlers
    await channel.basic_consume(simple_message__declared.queue, handlers.simple_message)
    await channel.basic_consume(ping_pong__declared.queue, handlers.ping_pong)


    # call internal__messager (3 common ways)
    send_message__internal_messager__declared = await channel.queue_declare("reminder24:internal__scheduler:send_message__internal_messager")

    send_message__internal_messager__declared_new = await channel.queue_declare("reminder24:internal__scheduler:imperial_test")

    call_upper_word__internal_messager__declared = await channel.queue_declare("reminder24:internal__scheduler:call_upper_word__internal_messager")
    call_upper_word_by_jsonrpc__internal_messager__declared = await channel.queue_declare("reminder24:internal__scheduler:call_upper_word_by_jsonrpc__internal_messager")

    await channel.basic_consume(send_message__internal_messager__declared.queue, handlers.send_message__internal_messager)

    await channel.basic_consume(send_message__internal_messager__declared_new.queue, handlers.send_message__internal_messager_new)

    await channel.basic_consume(call_upper_word__internal_messager__declared.queue, handlers.call_upper_word__internal_messager)
    await channel.basic_consume(call_upper_word_by_jsonrpc__internal_messager__declared.queue, handlers.call_upper_word_by_jsonrpc__internal_messager)

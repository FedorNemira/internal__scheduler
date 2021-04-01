from aio_pika import connect_robust
from aio_pika.patterns import RPC
from termcolor import cprint

from rpc import methods
from settings import AMQP_URI


async def rpc_subscriptions():

    connection = await connect_robust(
        AMQP_URI,
    )

    channel = await connection.channel()

    rpc = await RPC.create(channel)
    await rpc.register("internal__monitor__upper", methods.internal__monitor__upper, auto_delete=True)

    cprint("AMQP RPC:          ready [yes]", "green")
    return connection

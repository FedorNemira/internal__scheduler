import asyncio
import json

import aio_pika
from aio_pika import connect_robust
from aio_pika.patterns import RPC
from simple_print.functions import sprint_f

from database import methods as db_methods
from settings import AMQP_URI


class Publisher:
    @classmethod
    async def create(self, *args, **kwargs):
        self = Publisher()
        self.loop = asyncio.get_event_loop()
        self.connection = await connect_robust(AMQP_URI, loop=self.loop)
        return self


    async def send_message__internal_messager(self, word: str):
        sprint_f(f"send_message__internal_messager :: {word}")

        async with self.connection:
            routing_key = "reminder24:internal__messager:test_message"
            channel = await self.connection.channel()

            await channel.default_exchange.publish(
                aio_pika.Message(body=f"Hello {word}".encode()),
                routing_key=routing_key,
            )
        return
    
    async def send_message__internal_messager(self, word: dict):


        async with self.connection:
            routing_key = "reminder24:internal__messager:telegram_send_message"
            channel = await self.connection.channel()

            await channel.default_exchange.publish(
                aio_pika.Message(body=json.dumps(word).encode()),
                routing_key=routing_key,
            )

        return 
    

    async def send_message__internal_messager_new(self, word: str):
        sprint_f(f"send_message__internal_messager :: {word}")

        async with self.connection:
            routing_key = "reminder24:internal__messager:imperial_test"
            channel = await self.connection.channel()
            d = {}
            d['host'] = word
            await channel.default_exchange.publish(
                
                aio_pika.Message(body=json.dumps(d).encode()),
                routing_key=routing_key,
            )

        return

    async def call_upper_word__internal_messager(self, word: str):
        sprint_f(f"call_upper_word__internal_messager :: {word}")

        async with self.connection:
            channel = await self.connection.channel()
            rpc = await RPC.create(channel)
            upper_word = await rpc.proxy.upper_word__internal_messager(word=word)
        return upper_word

    async def call_upper_word_by_jsonrpc__internal_messager(self, json_rq):
        sprint_f(f"call_upper_word_by_jsonrpc__internal_messager :: {json_rq}")

        async with self.connection:
            channel = await self.connection.channel()
            rpc = await RPC.create(channel)
            upper_word = await rpc.proxy.internal_messager__upper_word_as_json_rpc(json_rq)
        return upper_word

import pprint
import pytest
from consumer import methods
from database import methods
from publisher.methods import Publisher


@pytest.mark.asyncio
async def test_send_message__internal_messager():
    messages = await methods.select_sheduled_message()
    pprint.pprint(messages)
    for message in messages: 
        publisher = await Publisher.create()
        result = await publisher.send_message__internal_messager(message)
        assert result

import re

mystr = 'This is a string, with words!'
wordList = re.sub("[^\w]", " ",  mystr).split()
import aiocron
from publisher.methods import Publisher
from database import methods


@aiocron.crontab("*/1 * * * *", start=False)
async def scheduler():
    messages = await methods.select_sheduled_message()
    for message in messages:
        publisher = await Publisher.create()
        await publisher.send_message__internal_messager(message)

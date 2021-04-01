import datetime

import aiormq.types
import ujson
from pydantic import ValidationError
from simple_print.functions import sprint_f

from settings import DEBUG


def validate_request_schema(request_schema):
    def wrap(func):
        async def wrapped(message: aiormq.types.DeliveredMessage):
            now = datetime.datetime.now().time()
            await message.channel.basic_ack(message.delivery.delivery_tag)
            sprint_f(f"\n\n~ {func.__name__} :: basic_ack [OK] :: {now}", "green")

            json_rq = None
            request = None
            response = None
            error = None

            try:
                json_rq = ujson.loads(message.body)
                request = request_schema.validate(json_rq).dict()
            except ValidationError as error_message:
                error = f"~ ERROR REQUEST, VALIDATION ERROR: body={message.body} error={error_message}"
            except Exception as error_message:
                error = f"~ ERROR REQUEST: body={message.body} error={error_message}"

            if not error:
                sprint_f(f"~ {func.__name__} :: Request {json_rq}", "yellow")
                try:
                    response = await func(request)
                except Exception as error_message:
                    error = f"~ ERROR RESPONSE: body={message.body} error={error_message}"

            if DEBUG:
                if error:
                    sprint_f(error, "red")
                else:
                    sprint_f(f"~ {func.__name__} :: complete [OK]", "green")
                    sprint_f(f"~ {func.__name__} :: Response {response}", "yellow")

        return wrapped

    return wrap

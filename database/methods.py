import pprint
from termcolor import cprint
import asyncpg
from simple_print.functions import sprint
from settings import DATABASE_URI
from datetime import datetime

async def select_sheduled_message(test=False):
    
    conn = await asyncpg.connect(DATABASE_URI)

    month = int(datetime.today().strftime('%m')) 
    day = int(datetime.today().strftime('%d'))
    hour = int(datetime.today().strftime('%H'))
    minute = int(datetime.today().strftime('%M'))
    
    if test:
        month = 3
        day = 21
        hour = 18
        minute = 30

    sheduled_message_records = f"""  
    SELECT *
    FROM user_profile_sheduledmessage
    WHERE (EXTRACT('hour' FROM "user_profile_sheduledmessage"."schedule_time" AT TIME ZONE 'Europe/Moscow') = {hour} 
    AND EXTRACT('minute' FROM "user_profile_sheduledmessage"."schedule_time" AT TIME ZONE 'Europe/Moscow') = {minute}
    AND EXTRACT('day' FROM "user_profile_sheduledmessage"."schedule_time" AT TIME ZONE 'Europe/Moscow') = {day}
    AND EXTRACT('month' FROM "user_profile_sheduledmessage"."schedule_time" AT TIME ZONE 'Europe/Moscow') = {month})
    """
    if test:
        sprint(sheduled_message_records, 'yellow')
    try:
        sheduled_message_records = await conn.fetch(sheduled_message_records)
        if test:
            sprint(sheduled_message_records, 'yellow')
    except Exception as e:
        sheduled_message_records = []
    finally:
        await conn.close()

    response = []
    for sheduled_message_record in sheduled_message_records:
        sheduled_message_records_dict = {}
        sheduled_message_records_dict["text"] = str(sheduled_message_record["text"])
        sheduled_message_records_dict["schedule_time"] = str(sheduled_message_record["schedule_time"])
        sheduled_message_records_dict["chat_id"] = str(sheduled_message_record["telegram_chat_id"])
        response.append(sheduled_message_records_dict)

    if test:
        pprint.pprint(response)
        if not response:
            response.append(1)

    
    return response




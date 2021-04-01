import pprint
import sys
import pytest
import asyncpg
from database import methods
from settings import DATABASE_URI

sys.path.append('..')

@pytest.mark.asyncio
async def test_select_sheduled_message():
    
    result = await methods.select_sheduled_message(test=True)
    pprint.pprint(result)
    assert result


# @pytest.mark.asyncio
# async def test_filling_database_select_sheduled_message(test=True):
    
#     for i in range(24):
#         for j in range(60):

#             conn = await asyncpg.connect(DATABASE_URI)

#             print(i)

#             sheduled_message_records = f"""  
#             INSERT INTO user_profile_sheduledmessage
#             VALUES (7{j}{i}, 218865388, 'Test{j}__{i}', '2021-03-22 {i:02}:{j:02}:00+00:00', '2021-03-21 08:07:28.607810+00:00', 1);

#             """
            
#             print(sheduled_message_records)

#             try:
#                 sheduled_message_records = await conn.fetch(sheduled_message_records)
#             except:
#                 sheduled_message_records = []
#             finally:
#                 await conn.close()
 
#     return True
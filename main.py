import asyncio

from src.queries.core import create_tables, insert_data


create_tables()

asyncio.run(insert_data())


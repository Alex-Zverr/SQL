from sqlalchemy import select
from src.database import async_engine, engine, session_factory, async_session_factory, Base
from src.models import WorkersOrm


class SyncCore:
    @staticmethod
    def create_tables():
        engine.echo = False
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        engine.echo = True

    @staticmethod
    async def insert_data():
        worker_alex = WorkersOrm(username="Alex")
        worker_hello = WorkersOrm(username="Hello")
        worker_world = WorkersOrm(username="World")

        async with session_factory() as session:
            session.add_all([worker_alex, worker_hello, worker_world])
            await session.commit()


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all(engine))
            await conn.run_sync(Base.metadata.create_all(engine))

    @staticmethod
    async def insert_data():
        worker_alex = WorkersOrm(username="Alex")
        worker_hello = WorkersOrm(username="Hello")
        worker_world = WorkersOrm(username="World")

        async with async_session_factory() as session:
            session.add_all([worker_alex, worker_hello, worker_world])
            await session.commit()

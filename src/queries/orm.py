from sqlalchemy import select
from src.database import engine, session_factory, Base
from src.models import WorkersOrm


class SyncORM:
    @staticmethod
    def create_tables():
        engine.echo = False
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_data():
        worker_alex = WorkersOrm(username="Alex")
        worker_hello = WorkersOrm(username="Hello")
        worker_world = WorkersOrm(username="World")

        with session_factory() as session:
            session.add_all([worker_alex, worker_hello, worker_world])
            session.commit()

    @staticmethod
    def get_workers():
        with session_factory as session:
            query = select(WorkersOrm)
            result = session.execute(query)
            workers = result.all()
            print(f"{workers=}")

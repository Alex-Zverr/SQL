from sqlalchemy import select, func, cast, Integer, and_
from src.database import engine, session_factory, Base
from src.models import WorkersOrm, ResumesOrm, Workload


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
        worker_roman = WorkersOrm(username="Roman")
        worker_misha = WorkersOrm(username="Misha")
        worker_vica = WorkersOrm(username="Vica")

        with session_factory() as session:
            session.add_all([worker_alex, worker_roman, worker_misha, worker_vica])
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            query = select(WorkersOrm)
            result = session.execute(query)
            workers = result.scalars().all()
            print(f"{workers=}")

    @staticmethod
    def get_worker(worker_id: int = 2, new_username: str = "Misha"):
        with session_factory() as session:
            worker_michal = session.get(WorkersOrm, worker_id)
            worker_michal.username = new_username
            session.commit()

    @staticmethod
    def inset_resumes():
        alex_resume = ResumesOrm(title="Python Alex Senior", compensations="90000", workload=Workload.full_time, worker_id=1)
        roman_resume = ResumesOrm(title="Python Roman Junior", compensations="190000", workload=Workload.part_time, worker_id=2)
        misha_resume = ResumesOrm(title="Python Misha Bot", compensations="50000", workload=Workload.part_time, worker_id=3)
        vica_resume = ResumesOrm(title="Web Vica Good Programmer", compensations="60000", workload=Workload.full_time, worker_id=4)

        with session_factory() as session:
            session.add_all([alex_resume, roman_resume, misha_resume, vica_resume])
            session.commit()

    @staticmethod
    def select_resumes_avg_compensation(like_language: str = "Python"):
        with session_factory() as session:
            query = (
                select(
                    ResumesOrm.workload,
                    cast(func.avg(ResumesOrm.compensations), Integer).label("avg_compensation"),
                )
                .select_from(ResumesOrm)
                .filter(and_(
                    ResumesOrm.title.contains(like_language),
                    ResumesOrm.compensations > 40000,
                ))
                .group_by(ResumesOrm.workload)
                .having(cast(func.avg(ResumesOrm.compensations), Integer) > 70000)
            )
            print(query.compile(compile_kwargs={"literal_binds": True}))
            res = session.execute(query)
            result = res.all()
            print(result[0].avg_compensation)

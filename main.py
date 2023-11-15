from src.queries.orm import SyncORM

SyncORM.create_tables()
SyncORM.insert_data()
# SyncORM.select_workers()
SyncORM.get_worker(3, 'Misha')
SyncORM.inset_resumes()
SyncORM.select_resumes_avg_compensation()

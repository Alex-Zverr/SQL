import enum
from typing import Annotated

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
import datetime
import enum


int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('uts', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('uts', now())"),
                                                        onupdate=datetime.datetime.utcnow)]


class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[int_pk]
    username: Mapped[str]


class Workload(enum.Enum):
    part_time = "part_time"
    full_time = "full_time"


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[int_pk]
    title: Mapped[str]
    compensations: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    create_at: Mapped[created_at]
    updated_at: Mapped[updated_at]



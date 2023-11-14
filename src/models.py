from sqlalchemy import Table, MetaData, Integer, Column, String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class WorkersOrm(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]

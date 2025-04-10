from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Table(Base):
    __tablename__ = 'tables'

    name: Mapped[str] = mapped_column(unique=True)
    seats: Mapped[int]
    location: Mapped[str]

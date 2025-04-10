from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Table(Base):
    __tablename__ = 'tables'

    name: Mapped[str] = mapped_column(unique=True)
    seats: Mapped[int]
    location: Mapped[str]
    
    _table_args__ = (
        CheckConstraint(
            'seats > 0',
            name='check_seats_positive'
        ),
    )

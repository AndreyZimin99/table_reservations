from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    CheckConstraint,
    String,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    customer_name: Mapped[str] = mapped_column(String(32))
    table_id: Mapped[int] = mapped_column(
        ForeignKey('tables.id')
    )
    reservation_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    duration_minutes: Mapped[int]

    _table_args__ = (
        UniqueConstraint(
            'table_id',
            'reservation_time',
            name='uix_table_time'
        ),
        CheckConstraint(
            'duration_minutes > 0',
            name='check_duration_positive'
        ),
    )

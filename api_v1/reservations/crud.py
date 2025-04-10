from datetime import datetime, timezone

from fastapi import HTTPException, status

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Reservation

from .schemas import ReservationCreate


async def get_reservations(session: AsyncSession) -> list[Reservation]:
    stmt = select(Reservation).order_by(Reservation.id)
    result: Result = await session.execute(stmt)
    reservations = result.scalars().all()
    return list(reservations)


async def get_reservation(
    session: AsyncSession,
    reservation_id: int
) -> Reservation | None:
    return await session.get(Reservation, reservation_id)


async def create_reservation(
    session: AsyncSession,
    reservation_in: ReservationCreate
) -> Reservation:
    reservation = Reservation(**reservation_in.model_dump())
    if reservation.reservation_time < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Некоректное время бронирования'
        )
    existing_reservation = await session.execute(
        select(Reservation).filter(
            (Reservation.table_id == reservation.table_id) &
            (Reservation.reservation_time == reservation.reservation_time)
        )
    )

    if existing_reservation.scalars().first() is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f'Стол {reservation.table_id} забронирован на указанное время.'
            )
        )

    session.add(reservation)
    await session.commit()
    return reservation


async def delete_reservation(
    session: AsyncSession,
    reservation: Reservation,
) -> None:
    await session.delete(reservation)
    await session.commit()

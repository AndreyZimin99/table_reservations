from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper
from .schemas import Reservation, ReservationCreate


router = APIRouter(tags=['Reservation'])


@router.get('/', response_model=list[Reservation])
async def get_reservations(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.get_reservations(session=session)
    return result


@router.post('/',  response_model=Reservation)
async def create_reservation(
    reservation_in: ReservationCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_reservation(
        session=session,
        reservation_in=reservation_in
    )


@router.delete('/{reservation_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    reservation = await crud.get_reservation(
        session=session,
        reservation_id=reservation_id
    )
    if reservation:
        await crud.delete_reservation(session=session, reservation=reservation)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Стол {reservation_id} не найден'
        )

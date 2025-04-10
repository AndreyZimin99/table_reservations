from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper
from .schemas import Table, TableCreate

router = APIRouter(tags=['Table'])


@router.get('/', response_model=list[Table])
async def get_tables(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_tables(session=session)


@router.post('/',  response_model=Table)
async def create_table(
    table_in: TableCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_table(session=session, table_in=table_in)


@router.delete('/{table_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_reservation(
    table_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    table = await crud.get_table(session=session, table_id=table_id)
    if table:
        await crud.delete_table(session=session, table=table)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Стол {table_id} не найден'
        )

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Table

from .schemas import TableCreate


async def get_tables(session: AsyncSession) -> list[Table]:
    stmt = select(Table).order_by(Table.id)
    result: Result = await session.execute(stmt)
    tables = result.scalars().all()
    return list(tables)


async def get_table(session: AsyncSession, table_id: int) -> Table | None:
    return await session.get(Table, table_id)


async def create_table(session: AsyncSession, table_in: TableCreate) -> Table:
    table = Table(**table_in.model_dump())
    session.add(table)
    await session.commit()
    return table


async def delete_table(
    session: AsyncSession,
    table: Table,
) -> None:
    await session.delete(table)
    await session.commit()

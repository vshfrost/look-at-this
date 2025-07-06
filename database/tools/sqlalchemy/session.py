import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from database.tools.sqlalchemy.connection import ASYNC_DATABASE_URL


async def generate_async_session(async_database_url: str = ASYNC_DATABASE_URL) -> AsyncGenerator[AsyncSession, None]:
    is_logs_enabled = True if os.getenv("ENV", "prod") != "prod" else False

    engine = create_async_engine(async_database_url, echo=is_logs_enabled)
    async_session_local = async_sessionmaker(engine, expire_on_commit=False)

    async with async_session_local() as session:
        yield session



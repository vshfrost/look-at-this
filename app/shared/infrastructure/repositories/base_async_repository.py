from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.tools.sqlalchemy.session import generate_async_session


class BaseAsyncRepository:
    def __init__(self, session: AsyncSession = Depends(generate_async_session)):
        self._session = session

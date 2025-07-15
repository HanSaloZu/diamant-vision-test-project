from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import db_config

engine = create_async_engine(db_config.DB_URL)

create_new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with create_new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]

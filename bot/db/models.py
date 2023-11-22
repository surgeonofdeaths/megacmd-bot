from sqlalchemy import Column, Integer, String, BigInteger, Boolean
from db.base import Base
from db.database import engine

import asyncio


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), nullable=True)
    username = Column(String(length=255), nullable=False)
    telegram_id = Column(BigInteger)
    admin = Column(Boolean, default=False)

    def __str__(self):
        return f"{self.__class__.__name__}<id={self.id}, name={self.name}>"


# Base.metadata.create_all(bind=engine)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_models())

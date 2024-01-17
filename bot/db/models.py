from sqlalchemy import (
    Column, Integer, String, BigInteger, Boolean, ForeignKey, Text
)
from sqlalchemy_utils import EmailType
from db.base import Base
from db.database import engine

import asyncio
import bcrypt


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), nullable=True)
    username = Column(String(length=255), nullable=False)
    telegram_id = Column(BigInteger)
    admin = Column(Boolean, default=False)

    def __str__(self):
        return f"{self.__class__.__name__}<id={self.id}, name={self.name}>"


class Credential(Base):
    __tablename__ = "credential"

    id = Column(Integer, ForeignKey("users.id"))
    email = Column(EmailType)
    password = Column(Text)

    def verify_password(self, password):
        pwhash = bcrypt.hashpw(password, self.password)
        return self.password == pwhash


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_models())

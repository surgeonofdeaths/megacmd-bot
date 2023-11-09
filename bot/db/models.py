from sqlalchemy import Column, Integer, String, BigInteger
from db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), nullable=True)
    telegram_id = Column(BigInteger)

    def __str__(self):
        return f"{self.__class__.__name__}<id={self.id}, name={self.name}>"

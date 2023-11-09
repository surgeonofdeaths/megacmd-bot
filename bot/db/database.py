from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config.config import config

engine = create_async_engine(config)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

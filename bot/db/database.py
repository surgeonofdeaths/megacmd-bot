from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config.config import config


url = f"postgresql+psycopg2://postgres:{config.db.password}@" \
      f"{config.db.host}" \
      f"/{config.db.database}"
engine = create_async_engine(url)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()

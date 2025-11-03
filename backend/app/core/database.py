from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Async engine 생성
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # 개발 중 SQL 쿼리 로깅
    future=True,
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for models
Base = declarative_base()


# Dependency for getting DB session
async def get_db():
    """
    데이터베이스 세션을 제공하는 의존성
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

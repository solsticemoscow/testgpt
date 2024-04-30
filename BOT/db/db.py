from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from BOT.config import DB_MYSQL

ENGINE = create_async_engine(
    DB_MYSQL,
    echo=False,
    pool_pre_ping=True
)

async_session = async_sessionmaker(ENGINE, autoflush=True, expire_on_commit=False)
DB_SESSION = async_session()


import os

USER = os.getenv("DB_USER", "")
PASSWORD = os.getenv("DB_PASSWORD", "")
NAME = os.getenv("DB_NAME", "")
PORT = os.getenv("DB_PORT", "")

ASYNC_DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@db:{PORT}/{NAME}"

SYNC_DATABASE_URL = f"postgresql+psycopg://{USER}:{PASSWORD}@db:{PORT}/{NAME}"

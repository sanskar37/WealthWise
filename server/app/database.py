from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import DATABASE_URL

# This is a simplified engine setup that works directly with SQLite.
# The 'connect_args' is a specific requirement for using SQLite with web apps.
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, future=True
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 1. Where the database lives
DB_PATH = os.getenv("DB_PATH", "./tasks.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# 2. Engine = road (created ONCE)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite + FastAPI
)

# 3. Session factory (not a session yet)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# 4. Base = table registry
Base = declarative_base()

# Add this helper to a deps file later:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

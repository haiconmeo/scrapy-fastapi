"""deps"""
from typing import Generator
from fastapi.security import OAuth2PasswordBearer
from victim.core.config import settings
from victim.db.session import SessionLocal


def get_db() -> Generator:
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()






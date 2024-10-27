from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.search.search import SearchSchema


def searchAlumnus(data: SearchSchema, db: Session):
    pass


def searchHistory(db: Session):
    pass


def clearSearchHistory(db: Session):
    pass

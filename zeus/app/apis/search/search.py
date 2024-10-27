from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.schemas.search.search import SearchSchema
from app.cores.search.search import searchHistory, searchAlumnus, clearSearchHistory

router = APIRouter()
settings = load_app_settings()


@router.post('/alumnus/all', status_code=200, description='搜索校友')
def search_alumnus(
        data: SearchSchema,
        db: Session = Depends(get_rdbms)

):
    return searchAlumnus(data, db)


@router.get('/alumnus/history', status_code=200, description='搜索校友历史')
def search_history(
        db: Session = Depends(get_rdbms)

):
    return searchHistory(db)


@router.delete('/alumnus/clear', status_code=200, description='清空搜索校友历史')
def clear_search_history(
        db: Session = Depends(get_rdbms)

):
    return clearSearchHistory(db)

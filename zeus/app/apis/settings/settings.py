from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.schemas.user.user import User
from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.cores.user.user import get_current_user
from app.schemas.settings.settings import AddSettings, UpdateSettings
from app.cores.settings.settings import get_settings, add_setting, update_setting, delete_setting, getSettingByID, getSettingByName

router = APIRouter()

settings = load_app_settings()


@router.get('/all', status_code=200, description='获取所有配置')
def settings_list(
        setts: list = Depends(get_settings),
        # admin: User = Depends(get_current_user)
):
    return setts


@router.post('/add/setting', status_code=200, description='添加配置')
def add_settings(
        data: AddSettings,
        # admin: User = Depends(get_current_user),
        db: Session = Depends(get_rdbms)):
    return add_setting(data, db=db)


@router.patch('/update/setting/{id}', status_code=200, description='更新配置')
def update_settings(
        id: int,
        data: UpdateSettings,
        # admin: User = Depends(get_current_user),
        db: Session = Depends(get_rdbms)):
    return update_setting(id, data, db=db)


@router.get('/setting/id/{id}', status_code=200, description='通过id获取配置')
def get_setting_by_id(
        id: int,
        # admin: User = Depends(get_current_user),
        db: Session = Depends(get_rdbms)):
    return getSettingByID(id, db=db)


@router.get('/setting/name/{name}', status_code=200, description='通过名称获取配置')
def get_setting_by_name(
        name: str,
        # admin: User = Depends(get_current_user),
        db: Session = Depends(get_rdbms)):
    return getSettingByName(name, db=db)


@router.delete('/delete/setting/{id}', status_code=200, description='删除配置')
def delete_settings(
        id: int,
        # admin: User = Depends(get_current_user),
        db: Session = Depends(get_rdbms)):
    return delete_setting(id, db=db)

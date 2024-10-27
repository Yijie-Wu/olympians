import json

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from app.models import Config
from app.extensions import get_rdbms
from app.schemas.settings.settings import AddSettings, UpdateSettings


def get_settings(db: Session = Depends(get_rdbms)):
    settings = db.query(Config).all()

    return [{"id": config.id, "name": config.name, "content": config.content} for config in settings]


def add_setting(data: AddSettings, db: Session):
    config = db.query(Config).filter(Config.name == data.name).first()

    if config:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"设置 {data.name} 已存在")

    else:
        config = Config(name=data.name, content=str(data.content))
        db.add(config)
        db.commit()
        db.refresh(config)

        return {"id": config.id, "name": config.name, "content": config.content}


def update_setting(id: int, data: UpdateSettings, db: Session):
    config = db.query(Config).filter(Config.id == id).first()

    if config:
        config.name = data.name
        config.content = str(data.content)
        db.commit()
        db.refresh(config)

        return {"id": config.id, "name": config.name, "content": config.content}

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"设置 {data.name} 不存在")


def getSettingByID(id: int, db: Session):
    config = db.query(Config).filter(Config.id == id).first()

    if config:
        return json.loads(config.content)

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"设置ID {id} 不存在"
        )


def getSettingByName(name: str, db: Session):
    config = db.query(Config).filter(Config.name == name).first()

    if config:
        return json.loads(config.content)

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"设置ID {id} 不存在"
        )


def delete_setting(id: int, db: Session):
    config = db.query(Config).filter(Config.id == id).first()

    if config:
        db.delete(config)
        db.commit()
        return {'detail': '删除设置成功'}

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"设置ID {id} 不存在"
        )

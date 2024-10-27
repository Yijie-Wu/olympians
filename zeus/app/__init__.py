"""
程序初始化模块
"""
import sys


from loguru import logger
from fastapi import FastAPI

from app.apis import router
from app.models import Roles, User, Config
from app.middlewares import add_cors_middleware
from app.settings import Settings, load_app_settings, DATA_STORE_DIR
from app.extensions import generate_tables, SessionLocal
from app.utils.password import hash_password


def create_app() -> FastAPI:
    """
    创建FastAPI应用程序的函数
    :return: FastAPI实例
    """
    settings = load_app_settings()

    app = FastAPI(
        title=settings.APP.APP_TITLE,
        version=settings.APP.APP_VERSION,
        description=settings.APP.APP_DESCRIPTION
    )

    register_router(app, settings)
    init_dirs(settings)
    register_middlewares(app, settings)
    register_logging(settings)
    register_databases(settings)

    return app


def register_router(app: FastAPI, settings: Settings):
    """
    :param app:
    :param settings:
    :return:
    """
    app.include_router(router, prefix=settings.APP.GLOBAL_API_PREFIX)


def register_middlewares(app: FastAPI, settings: Settings):
    """
    :param app:
    :param settings:
    :return:
    """
    add_cors_middleware(app, settings)


def init_role_permissions():
    """
    :return:
    """
    roles = ["超级管理员", "管理员", "普通用户"]

    db = SessionLocal()
    for role in roles:
        role_check = db.query(Roles).filter(Roles.name == role).first()
        if not role_check:
            new_role = Roles(name=role)
            db.add(new_role)
            db.commit()
            db.refresh(new_role)

    db.close()


def init_admin(settings: Settings):
    """
    :param settings:
    :return:
    """
    db = SessionLocal()

    admin_check = db.query(User).filter(User.username == settings.APP.ADMIN_USERNAME).first()
    if not admin_check:
        admin = User(
            username=settings.APP.ADMIN_USERNAME,
            role_id=1,
            password_hash=hash_password('Passw0rd!')
        )

        db.add(admin)
        db.commit()
        db.refresh(admin)
    db.close()


def register_databases(settings: Settings):
    """
    :param settings:
    :return:
    """
    generate_tables()
    init_role_permissions()
    init_admin(settings)


def register_logging(settings: Settings):
    """
    :param settings:
    :return:
    """
    logger.remove()

    logger.add(
        sys.stdout,
        format=settings.LOGGING.FORMAT,
        level=settings.LOGGING.LEVEL,
        enqueue=settings.LOGGING.ENQUEUE,
        backtrace=settings.LOGGING.TRACEBACK,
        diagnose=settings.LOGGING.DIAGNOSE
    )


def init_dirs(settings: Settings):
    """
    :param settings:
    :return:
    """
    pass
    # if not os.path.exists(DATA_STORE_DIR):
    #     os.makedirs(DATA_STORE_DIR, exist_ok=True)
    #
    # if not os.path.exists(settings.APP.ALUMNUS_AVATARS_DIR):
    #     os.makedirs(settings.APP.ALUMNUS_AVATARS_DIR, exist_ok=True)
    #
    # if not os.path.exists(settings.APP.AVATARS_DIR):
    #     os.makedirs(settings.APP.AVATARS_DIR, exist_ok=True)
    #
    # if not os.path.exists(settings.APP.LOGS_DIR):
    #     os.makedirs(settings.APP.LOGS_DIR, exist_ok=True)

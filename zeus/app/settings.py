"""
设置模块，用于设置整个程序
"""

import os
import sys
from typing import List
from pathlib import Path

DATA_STORE_DIR = os.path.join(Path(__file__).parent.parent, 'olympians_data')


class Settings:
    class APP:
        APP_TITLE: str = 'Olympians'
        APP_VERSION: str = '0.0.1'
        APP_DESCRIPTION: str = '[olympians] 自动化测试系统.'
        BACKEND_SERVER: str = 'http://127.0.0.1:8000'

        GLOBAL_API_PREFIX: str = ''

        ACCESS_TOKEN_EXPIRE_MINUTES: int = 24 * 60 * 365
        JWT_SECRET_KEY: str = 'JWT_SECRET_KEY'
        JWT_ALGORITHM: str = 'HS256'
        ADMIN_USERNAME: str = 'root'
        LOGS_DIR: str = os.path.join(DATA_STORE_DIR, 'logs')
        AVATARS_DIR: str = os.path.join(DATA_STORE_DIR, 'avatars')
        BLOGS_VIDEO_DIR: str = os.path.join(DATA_STORE_DIR, 'blog-videos')
        BLOGS_IMAGE_DIR: str = os.path.join(DATA_STORE_DIR, 'blog-images')
        FRONT_IMAGE_DIR: str = os.path.join(DATA_STORE_DIR, 'front-images')

    class LOGGING:
        LEVEL: str = 'INFO'
        FORMAT: str = '{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{file}:{function}():{line} -> {message}'
        ENQUEUE: bool = True
        DIAGNOSE: bool = True
        TRACEBACK: bool = True
        LOG_NAME: str = 'olympians.log'

    class DB:
        AUTO_FLASH: bool = True
        PREFIX: str = 'sqlite:///' if sys.platform.startswith('win') else 'sqlite:////'
        DATABASE_URL: str = PREFIX + os.path.join(DATA_STORE_DIR, 'data.db')

    class CORS_MIDDLEWARE:
        ALLOW_METHODS: List[str] = ["*"]
        ALLOW_HEADERS: List[str] = ["*"]
        ALLOW_ORIGINS: List[str] = ["*", "http://127.0.0.1:5473"]
        ALLOW_CREDENTIALS: bool = True


def load_app_settings() -> Settings:
    settings = Settings()
    return settings

# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""

import os
import sys

basedir = os.path.dirname(os.path.dirname(__file__))

WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"


class BaseConfig:
    BASE_DIR = basedir
    SECRET_KEY = os.getenv("SECRET_KEY", "secret string")


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, "data.db")


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""

import os

from flask import Flask

from settings import config
from extensions import db


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "development")

    app = Flask("app")

    app.config.from_object(config[config_name])
    register_extensions(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)


def register_commands(app):
    @app.cli.command()
    def initdb():
        pass

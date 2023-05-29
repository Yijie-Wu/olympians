# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""

from fastapi import FastAPI


def create_app():
    app = FastAPI(title="Demeter", description="File server")

    register_router(app)

    return app


def register_router(app: FastAPI):
    from .api.v1 import api_router as router_v1
    app.include_router(router_v1)

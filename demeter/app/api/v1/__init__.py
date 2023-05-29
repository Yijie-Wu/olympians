# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""
from . import health
from . import fileops

from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(health.router, prefix='/v1', tags=['Demeter Health'])
api_router.include_router(fileops.router, prefix='/v1', tags=['Demeter Upload And Download'])

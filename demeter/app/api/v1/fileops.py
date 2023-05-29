# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""
from fastapi import APIRouter, Response

router = APIRouter()


@router.get('/demeter/upload', status_code=201)
def upload():
    return {"status": "ok"}


@router.get('/demeter/download', status_code=200)
def upload():
    return {"status": "ok"}
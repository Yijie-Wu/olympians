# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""
from fastapi import APIRouter, Response

router = APIRouter()


@router.get('/demeter/health-check')
def health_check(response: Response):
    response.status_code = 204
    return response

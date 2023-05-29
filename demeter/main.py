# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", reload=True)

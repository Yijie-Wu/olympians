"""
主程序入口
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app')

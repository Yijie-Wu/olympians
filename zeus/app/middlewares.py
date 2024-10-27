from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings import Settings


def add_cors_middleware(app: FastAPI, settings: Settings):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_MIDDLEWARE.ALLOW_ORIGINS,
        allow_credentials=settings.CORS_MIDDLEWARE.ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_MIDDLEWARE.ALLOW_METHODS,
        allow_headers=settings.CORS_MIDDLEWARE.ALLOW_HEADERS,
    )

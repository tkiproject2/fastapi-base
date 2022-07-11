from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class Middleware:
    def __init__(self, app: FastAPI) -> None:
        return app.add_middleware(
            CORSMiddleware,
            allow_origins=["*", "*"],
            allow_credentials=True,
            allow_methods=["*", "*"],
            allow_headers=["*", "*"],
        )

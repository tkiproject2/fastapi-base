from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI


class Middleware:
    def __init__(self,
    app: FastAPI) -> None:
        return app.add_middleware(
            CORSMiddleware,
            allow_origins=["*", "*"],
            allow_credentials=True,
            allow_methods=["*", "*"],
            allow_headers=["*", "*"],
        )
import http
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger
from starlette.exceptions import HTTPException as StarletteHTTPException

from config.config import MongoConnection
from route.company import router_company
from security.middleware import Middleware

app = FastAPI(openapi_url="/user_service/openapi.json", docs_url="/user_service/swgr")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.middleware("http")
async def http_middleware_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as err:
        logger.exception(err)
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "error": http.HTTPStatus(500).name.upper(),
                "type": "INTERNAL_SERVER_ERROR",
                "timestamp": datetime.now().isoformat(),
                "path": request.url.path,
                "params": request.url.query,
                "message": str(err),
            },
        )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "status": exception.status_code,
            "error": http.HTTPStatus(exception.status_code).name.upper(),
            "type": exception.detail["type"],
            "timestamp": datetime.now().isoformat(),
            "path": request.url.path,
            "params": request.url.query,
            "message": exception.detail["message"],
        },
    )


app = Middleware(app)


@app.get("/health", response_model=None)
async def health():
    """Health Check Fast Api"""
    return {"status": "ok"}


app.include_router(
    router_company,
    prefix="/user_service/company",
    tags=["company"],
    responses={404: {"description": "Not found"}},
)


@app.on_event("startup")
async def app_startup():
    """Start Fastapi"""
    MongoConnection


@app.on_event("shutdown")
async def app_shutdown():
    """Shutdown FastApi"""
    # config.close_db_client()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config.config import MongoConnection
from security.middleware import Middleware
from route.company import router_company

app = FastAPI(openapi_url="/user_service/openapi.json", docs_url="/user_service/swgr")
app.mount("/static", StaticFiles(directory="static"), name="static")

Middleware(app)

@app.get("/health", response_model=None)
async def health():
    """ Health Check Fast Api """    
    return {"status" : "ok"}

app.include_router(
    router_company,
    prefix="/user_service/company",
    tags=["company"],
    responses={404: {"description": "Not found"}},
)

@app.on_event("startup")
async def app_startup():    
    """ Start Fastapi """
    MongoConnection


@app.on_event("shutdown")
async def app_shutdown():
    """ Shutdown FastApi """
    # config.close_db_client()

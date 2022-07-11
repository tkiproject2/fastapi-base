import logging
from functools import lru_cache
from loguru import logger

import redis
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from .setting import load_config

# from document.company import CompanyDocument

CONF = load_config()

log = logging.getLogger("uvicorn")

config = load_config()


class Settings(BaseSettings):
    # App Config
    DEBUG: str = config.get("fastapi", dict())["debug"]
    SECRET_KEY: str = config.get("fastapi", dict())["key"]
    ENVIRONMENT: str = config.get("fastapi", dict())["environment"]
    PROJECT_NAME: str = config.get("fastapi", dict())["projectName"]
    TIMEZONE: str = config.get("fastapi", dict())["timezone"]

    # Mongo DB config
    db_mongo_host: str = config.get("mongodb-user", dict())["HOST"]
    db_mongo_port: int = config.get("mongodb-user", dict())["PORT"]
    db_mongo_user: str = config.get("mongodb-user", dict())["USER"]
    db_mongo_pass: str = config.get("mongodb-user", dict())["PASSWORD"]
    db_mongo_name: str = config.get("mongodb-user", dict())["NAME"]

    # Redis Data config
    redis_data_host: str = config.get("redis-data", dict())["HOST"]
    redis_data_port: int = config.get("redis-data", dict())["PORT"]
    redis_data_user: str = None
    redis_data_pass: str = None

    # Redis Queue config
    redis_queue_host: str = config.get("redis-data", dict())["HOST"]
    redis_queue_port: int = config.get("redis-data", dict())["PORT"]
    redis_queue_user: str = None
    redis_queue_pass: str = None

    # Client Base URL config
    auth_service: str = config.get("client-base-url", dict())["auth-service"]
    user_service: str = config.get("client-base-url", dict())["user-service"]
    notif_service: str = config.get("client-base-url", dict())["notif-service"]


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()


class MongoConnection:
    __instance = None

    async def __new__(self):
        if self.__instance is not None:
            logger.info(f"Using exsisting instance: {self.__instance}")
            return self.__instance

        return self.__init__(self)

    async def __init__(self):
        logger.info("Initialization new instance")
        client = AsyncIOMotorClient(
            host=Settings().db_mongo_host,
            port=Settings().db_mongo_port,
            username=Settings().db_mongo_user,
            password=Settings().db_mongo_pass,
        )
        self.__instance = client
        await init_beanie(database=client[Settings().db_mongo_name], document_models=[])

        return client

    def close(self):
        logger.info(f"Close instance connection: {self.__instance}")
        self.__instance.close()


# MGDB_CLIENT = AsyncIOMotorClient(
#     host=Settings().db_mongo_host,
#     port=Settings().db_mongo_port,
#     username=Settings().db_mongo_user,
#     password=Settings().db_mongo_pass,
# )

# MGDB = MGDB_CLIENT[Settings().db_mongo_name]


class RedisDataConnection:
    def __init__(self) -> None:
        return redis.Redis(
            host=Settings().redis_data_host,
            port=Settings().redis_data_port,
            db=0,
        )


class RedisQueueConnection:
    def __init__(self) -> None:
        return redis.Redis(
            host=Settings().redis_queue_host,
            port=Settings().redis_queue_port,
            db=0,
        )

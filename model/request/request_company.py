import ipaddress
from aiohttp import request
from bson.objectid import ObjectId
from enum import Enum
from pydantic import BaseModel, Field
from typing import Any, List
from datetime import datetime, date
from beanie import PydanticObjectId
from model.model_default import AddressData
from util.util_generate import RandomNumber, RandomString
from faker import Faker

fake = Faker()

class CreateCompanyRequest(BaseModel):
    name: str = None
    initial: str = None
    address: AddressData = None
    tags: List[str] = []
    picName: str = None
    picEmail: str = None
    picPhone: str = None
    maxUser: int = 0

    class Config:
        schema_extra = {
            "example": {
                "name": "PT " + fake.name(),
                "initial": RandomString(2),
                "address": {"street": fake.address()},
                "tags": [],
                "picName": fake.name(),
                "picEmail": fake.first_name() + "@coba.com",
                "picPhone": "0813" + RandomNumber(6),
                "maxUser": 1000,
            }
        }
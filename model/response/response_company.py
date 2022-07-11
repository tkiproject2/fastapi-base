import ipaddress
from datetime import date, datetime
from enum import Enum
from typing import Any, List

import faker
from aiohttp import request
from beanie import PydanticObjectId
from bson.objectid import ObjectId
from pydantic import BaseModel, Field

from document.company import CompanyDocument
from model.model_default import AddressData, ResponseModel
from util.util_generate import RandomNumber, RandomString


class CreateCompanyResponse(ResponseModel):
    data: CompanyDocument = None

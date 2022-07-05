import ipaddress
from aiohttp import request
from bson.objectid import ObjectId
from enum import Enum
from pydantic import BaseModel, Field
from typing import Any, List
from datetime import datetime, date
from beanie import PydanticObjectId
from model.model_default import AddressData, ResponseModel
from util.util_generate import RandomNumber, RandomString
import faker
from document.company import CompanyDocument

class CreateCompanyResponse(ResponseModel):
    data: CompanyDocument = None
import ipaddress
from datetime import date, datetime
from enum import Enum
from typing import Any, List

from aiohttp import request
from beanie import PydanticObjectId
from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class JwtToken(BaseModel):
    tblName: str = None
    userId: PydanticObjectId = None
    companyId: PydanticObjectId = None
    roles: List[str] = []
    isAdmin: bool = False
    exp: int = 1000
    lang: str = "id"


class JwtGateway(JwtToken):
    createTime: datetime = datetime.now()
    updateTime: datetime = datetime.now()
    sessionId: str = None
    key1: str = None
    key2: List[str] = []
    ipaddress: List[str] = []
    deviceIdentity: str = None


class Token(BaseModel):
    access_token: str
    token_type: str


class JwtBase(JwtToken):
    id: str = None
    jwtKey: str = None
    expiredTime: datetime = None
    ip: str = None


# ================================================================


class DefaultData(BaseModel):
    createTime: datetime = datetime.now()
    updateTime: datetime = datetime.now()
    companyId: PydanticObjectId = None  # bank
    creatorUserId: PydanticObjectId = None
    isDelete: bool = False


class DefaultPage(BaseModel):
    status: int = 200
    size: int = 0
    page: int = 0
    totalElements: int = 0
    totalPages: int = 0
    sort: int = 0
    sortDirection: str = None


# Address Default Model
# =================================================================
class ProvinceBase(BaseModel):
    id: str = None
    name: str = None


class RegencyBase(BaseModel):
    id: str = None
    province_id: str = None
    name: str = None


class DistrictBase(BaseModel):
    id: str = None
    regency_id: str = None
    name: str = None


class EmailData(BaseModel):
    name: str = None
    projectName: str = None
    companyName: str = None
    emailTo: str = None
    token: str = None


class CoordinateData(BaseModel):
    type: str = "Point"
    coordinates: List[float] = []


class AddressData(BaseModel):
    province: str = None
    city: str = None
    district: str = None
    village: str = None
    street: str = None
    posCode: str = None
    location: CoordinateData = None
    note: str = None


# Client Response Default Model
# =================================================================
class ClientHttpBasicAuth(BaseModel):
    username: str
    password: str


class ClientResponseModel(BaseModel):
    requestTime: datetime = None
    method: str = None
    urlRequest: str = None
    requestParam: Any = None
    headers: Any = None
    statusCode: int = None
    contentType: str = None
    responseHeaders: Any = None
    responseBody: Any = None
    responseTime: datetime = None


# Default Success Response Model
# =================================================================


class ResponseModel(BaseModel):
    status_code: int
    message: str
    data: Any = None

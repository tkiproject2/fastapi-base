from datetime import datetime
import json
import aiohttp
from aiohttp import BasicAuth
import asyncio
from model.model_default import ClientHttpBasicAuth, ClientResponseModel
from util.util_http_exception import BadRequestException
from model.enum.enum_exception import BadRequestExceptionMessage
from loguru import logger

async def getRequestClient(url: str, param: dict = None, headers: dict = None, httpBasic: ClientHttpBasicAuth = None) -> ClientResponseModel:
    response = ClientResponseModel()
    response.requestTime = datetime.now()
    response.urlRequest = url
    response.method = "GET"
    response.requestParam = param
    response.headers = headers

    if httpBasic:
        async with aiohttp.ClientSession(headers=headers).auth(BasicAuth(httpBasic.username, httpBasic.password)) as session:
            try:
                async with session.get(url=url) as resp:            
                    response.statusCode = resp.status
                    response.responseHeaders = resp.headers
                    response.responseBody = await resp.json()            
                    response.responseTime = datetime.now()
                    return response
            except Exception as e:
                logger.warning(e)
                raise BadRequestException(BadRequestExceptionMessage.FAILED_TO_REQUEST)
    else:
        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.get(url=url) as resp:            
                    response.statusCode = resp.status
                    response.responseHeaders = resp.headers
                    response.responseBody = await resp.json()            
                    response.responseTime = datetime.now()
                    return response
            except Exception as e:
                logger.warning(e)
                raise BadRequestException(BadRequestExceptionMessage.FAILED_TO_REQUEST)



async def postRequestClient(url: str, param: dict = None, requestBody : dict = None, headers: dict = None, httpBasic: ClientHttpBasicAuth = None) -> ClientResponseModel:
    response = ClientResponseModel()
    response.requestTime = datetime.now()
    response.urlRequest = url
    response.method = "GET"
    response.requestParam = param
    response.headers = headers

    payload = json.dumps(requestBody)

    if httpBasic:
        async with aiohttp.ClientSession(headers=headers).auth(BasicAuth(httpBasic.username, httpBasic.password)) as session:
            try:
                async with session.post(url=url, data=payload) as resp:            
                    response.statusCode = resp.status
                    response.responseHeaders = resp.headers
                    response.responseBody = await resp.json()            
                    response.responseTime = datetime.now()
                    return response
            except Exception as e:
                logger.warning(e)
                raise BadRequestException(BadRequestExceptionMessage.FAILED_TO_REQUEST)
    else:
        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.post(url=url, data=payload) as resp:            
                    response.statusCode = resp.status
                    response.responseHeaders = resp.headers
                    response.responseBody = await resp.json()            
                    response.responseTime = datetime.now()
                    return response
            except Exception as e:
                logger.warning(e)
                raise BadRequestException(BadRequestExceptionMessage.FAILED_TO_REQUEST)
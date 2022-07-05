# ===== Module & Library
from http import HTTPStatus
from typing import Any

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from model.enum.enum_response_message import *

# ===== Header

# ===== Function

# ===== Class
# 2xx

# 3xx
class NotModifiedException(HTTPException):
    def __init__(
        self,
        detail: Any = NotModifiedErrorMessage,
    ) -> None:
        super().__init__(status_code=HTTPStatus.NOT_MODIFIED.value, detail=detail)


# 4xx
class BadRequestException(HTTPException):
    def __init__(
        self,
        detail: BadRequestExceptionMessage = None,
    ) -> None:
        super().__init__(status_code=HTTPStatus.BAD_REQUEST.value, detail=detail)
        # super().__init__(HTTPException (status_code = HTTPStatus.BAD_REQUEST, content = {"status_code" : HTTPStatus.BAD_REQUEST, "message": detail}))



class UnauthorizedException(HTTPException):
    def __init__(
        self,
        detail: UnauthorizedExceptionMessage = None,
    ) -> None:
        super().__init__(status_code=HTTPStatus.UNAUTHORIZED.value, detail=detail)


class ForbiddenException(HTTPException):
    def __init__(
        self,
        detail: ForbidenExceptionMessage = None,
    ) -> None:
        super().__init__(status_code=HTTPStatus.FORBIDDEN.value, detail=detail)


class NotFoundException(HTTPException):
    def __init__(
        self,
        detail: NotFoundExceptionMessage = None,
    ) -> None:
        super().__init__(status_code=HTTPStatus.NOT_FOUND.value, detail=detail)


# 5xx
class InternalServerErrorException(HTTPException):
    def __init__(
        self,
        detail: InternalServerErrorExceptionMessage = None,
    ) -> None:
        super().__init__(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value, detail=detail
        )



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
        type=NotModifiedErrorMessage,
        message: str = "",
    ) -> None:
        super().__init__(
            status_code=HTTPStatus.NOT_MODIFIED.value,
            detail={"type": type, "message": message},
        )


# 4xx
class BadRequestException(HTTPException):
    def __init__(
        self,
        type: BadRequestExceptionMessage,
        message: str = "",
    ) -> None:
        super().__init__(
            status_code=HTTPStatus.BAD_REQUEST.value,
            detail={"type": type, "message": message},
        )


class UnauthorizedException(HTTPException):
    def __init__(
        self,
        type: UnauthorizedExceptionMessage,
        message: str = "",
    ) -> None:
        super().__init__(
            status_code=HTTPStatus.UNAUTHORIZED.value,
            detail={"type": type, "message": message},
        )


class ForbiddenException(HTTPException):
    def __init__(
        self,
        type: ForbidenExceptionMessage,
        message: str = "",
    ) -> None:
        super().__init__(
            status_code=HTTPStatus.FORBIDDEN.value,
            detail={"type": type, "message": message},
        )


class NotFoundException(HTTPException):
    def __init__(
        self,
        type: NotFoundExceptionMessage,
        message: str = "",
    ) -> None:
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail={"type": type, "message": message},
        )


# 5xx
class InternalServerErrorException(HTTPException):
    def __init__(
        self, type: InternalServerErrorExceptionMessage, message: str = ""
    ) -> None:
        super().__init__(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail={"type": type, "message": message},
        )

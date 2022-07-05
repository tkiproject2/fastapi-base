from typing import Any
from fastapi.responses import JSONResponse
from model.enum.enum_response_message import SuccessMessage
from model.model_default import ResponseModel

def SuccessResponse(
        data: Any,
        message: SuccessMessage = SuccessMessage.OK,
        status_code: int = 200
    ):
        ResponseModel(status_code=status_code, message=message, data=data)
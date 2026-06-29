from fastapi import Request
from fastapi.responses import JSONResponse

from quantum_core.core.responses import APIResponse


class AppException(Exception):

    def __init__(
        self,
        message: str,
        status_code: int = 400
    ):
        self.message = message
        self.status_code = status_code


async def app_exception_handler(
    request: Request,
    exc: AppException
):

    return APIResponse.error(
        message=exc.message,
        status_code=exc.status_code
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error"
        }
    )
from fastapi import status, Request
from fastapi.responses import JSONResponse


async def default_error_handler(_: Request, exception: Exception) -> JSONResponse:
    error = str(exception)
    print(error)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal server error", "error": error}
    )
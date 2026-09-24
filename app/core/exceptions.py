from fastapi import Request, HTTPException, status, FastAPI
from fastapi.responses import JSONResponse



def register_exception_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def http_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    # @app.exception_handler(Exception)
    # async def general_exception_handler(request: Request, exc: Exception):
    #     return JSONResponse(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         content={"detail": "Internal Server Error"},
    #     )
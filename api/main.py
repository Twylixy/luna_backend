import logging
import os
from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from api.responses.error import ErrorResponse
from api.routes import api_router

logging.basicConfig(
    format='%(levelname)s - %(name)s:\t%(message)s',
    level=int(os.getenv('LOGGING_LEVEL', logging.INFO)),
)

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')
app.include_router(api_router)


@app.exception_handler(500)
async def internal_server_error_handler(
    request: Request, exception: Exception
) -> JSONResponse:
    """
    Handle 500 errors.

    Args:
        request: Request
        exception: Exception
    Returns:
        ErrorResponse
    """
    logging.log(logging.ERROR, "500 Internal Server Error: (%s)", exception)
    logging.log(
        logging.ERROR,
        "Url: {0}\nPath params: {1}\nQuery params: {2}\nHeaders: {3}\nBody: {4}".format(
            request.url,
            request.path_params,
            request.query_params,
            request.headers,
            request.body,
        ),
    )

    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            status='failure',
            message='Internal Server Error (500)',
        ).dict(),
    )


def custom_openapi() -> Dict[str, Any]:
    """
    Define OpenAPI overwrites for documentation.

    Returns:
        Dict[str, Any]: OpenAPI schema.
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title='Luna API',
        version='v1',
        description='The API service for Luna Discord Bot',
        routes=app.routes,
        contact={
            'name': 'The Staypony',
            'url': os.getenv('SWAGGER_URL', 'https://staypony.space'),
            'email': os.getenv('SWAGGER_EMAIL', 'admin@staypony.space'),
        },
        license_info={
            'name': 'BSD License',
        },
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# this line ignored because of bug in mypy
app.openapi = custom_openapi  # type: ignore[assignment]

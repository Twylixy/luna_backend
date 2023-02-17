from fastapi import APIRouter

from api.responses.status.healthcheck import HealthcheckResponse

healthcheck_router = APIRouter()


@healthcheck_router.get('/healthcheck', response_model=HealthcheckResponse)
async def healthcheck() -> HealthcheckResponse:
    """
    Return status for healthcheck.

    Returns:
        HealthcheckResponse
    """
    return HealthcheckResponse(
        status='success',
        message='API operational',
    )

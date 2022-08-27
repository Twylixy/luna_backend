from fastapi import APIRouter

from api.responses.status.healthcheck import HealthcheckResponse

router = APIRouter(prefix='/api/status', tags=['status'])


@router.get('/healthcheck', response_model=HealthcheckResponse)
def healthcheck() -> HealthcheckResponse:
    """
    Return status for healthcheck.

    Returns:
        HealthcheckResponse
    """
    response = {
        'status': 'success',
        'message': 'API operational',
    }
    return HealthcheckResponse.parse_obj(response).dict()

from fastapi import APIRouter
from app.core.config import settings
from app.schemas.health import HealthResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check",
    description="Check whether the API server is healthy and running.",
)
def check_health() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        app_name=settings.app_name,
        environment=settings.app_env,
        version="0.1.0",
    )

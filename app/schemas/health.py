from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(..., description="Application health status")
    app_name: str = Field(..., description="Application name")
    environment: str = Field(..., description="Current deployment environment")
    version: str = Field(default="0.1.0", description="API version")

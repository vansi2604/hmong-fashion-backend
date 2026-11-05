from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: logic before application begins accepting requests
    yield
    # Shutdown: clean up resources (e.g., database connections)


def create_app() -> FastAPI:
    application = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="RESTful Backend API for Hmong Fashion E-commerce platform",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # CORS middleware for Next.js frontend communication
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # API v1 routes
    application.include_router(api_router, prefix="/api/v1")

    @application.get("/", tags=["Root"])
    def root():
        return {
            "message": f"Welcome to {settings.app_name}",
            "version": "0.1.0",
            "docs": "/docs",
            "health": "/api/v1/health",
        }

    return application


app = create_app()

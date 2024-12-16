from fastapi import FastAPI

# Router Imports
from portfolio.routers.missions.missions import router as missions_router
from portfolio.routers.projects.project import router as project_router
from portfolio.routers.users.users import router as users_router
# Config Imports
from portfolio.core.config import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION
    )
    
    # Inclure les routes
    application.include_router(missions_router, prefix=f"{settings.API_PREFIX}/missions")
    application.include_router(project_router, prefix=f"{settings.API_PREFIX}/projects")
    application.include_router(users_router, prefix=f"{settings.API_PREFIX}/users")
    
    return application


app = get_application()

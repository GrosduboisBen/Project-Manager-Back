from fastapi import FastAPI
from portfolio.core.config import settings

# Import routers
from portfolio.routers.users.users import router as users_router
from portfolio.routers.projects.projects import router as projects_router
from portfolio.routers.missions.missions import router as missions_router
from portfolio.routers.milestones.milestones import router as milestones_router
from portfolio.routers.roles.roles import router as roles_router
# Import other routers as you add them

# Create the FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

# Include routers
app.include_router(users_router, prefix=f"{settings.API_PREFIX}/users", tags=["Users"])
app.include_router(projects_router, prefix=f"{settings.API_PREFIX}/projects", tags=["Projects"])
app.include_router(missions_router, prefix=f"{settings.API_PREFIX}/missions", tags=["Missions"])
app.include_router(milestones_router, prefix=f"{settings.API_PREFIX}/milestones", tags=["Milestones"])
app.include_router(roles_router, prefix=f"{settings.API_PREFIX}/roles", tags=["Roles"])
# Add additional routes as necessary

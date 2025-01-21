from fastapi import FastAPI
from portfolio.core.config import settings

# Import routers
from portfolio.routers.users.users import router as users_router
from portfolio.routers.projects.projects import router as projects_router
from portfolio.routers.missions.missions import router as missions_router
from portfolio.routers.milestones.milestones import router as milestones_router
from portfolio.routers.roles.roles import router as roles_router
from portfolio.routers.permissions.permissions import router as permissions_router
from portfolio.routers.technologies.technologies import router as technologies_router
from portfolio.routers.tags.tags import router as tags_router
from portfolio.routers.pricing.pricing import router as pricing_router
from portfolio.routers.feedbacks.feedbacks import router as feedbacks_router
from portfolio.routers.invoices.invoices import router as invoices_router
from portfolio.routers.invoices_infos.invoices_infos import router as invoices_info_router
from portfolio.routers.custom_blocks.custom_blocks import router as custom_blocks_router
from portfolio.routers.invoices_has_blocks.invoices_has_blocks import router as invoices_has_blocks_router
from portfolio.routers.calendars.calendars import router as calendars_router



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
app.include_router(permissions_router, prefix=f"{settings.API_PREFIX}/permissions", tags=["Permissions"])
app.include_router(technologies_router, prefix=f"{settings.API_PREFIX}/technologies", tags=["Technologies"])
app.include_router(tags_router, prefix=f"{settings.API_PREFIX}/tags", tags=["Tags"])
app.include_router(pricing_router, prefix=f"{settings.API_PREFIX}/pricing", tags=["Pricing"])
app.include_router(feedbacks_router, prefix=f"{settings.API_PREFIX}/feedbacks", tags=["FeedBacks"])
app.include_router(invoices_router, prefix=f"{settings.API_PREFIX}/invoices", tags=["Invoices"])
app.include_router(invoices_info_router, prefix=f"{settings.API_PREFIX}/invoices_infos", tags=["Invoices Infos"])
app.include_router(custom_blocks_router, prefix=f"{settings.API_PREFIX}/custom_blocks", tags=["Custom Blocks"])
app.include_router(invoices_has_blocks_router, prefix=f"{settings.API_PREFIX}/invoices_blocks", tags=["Invoices Blocks"])
app.include_router(calendars_router, prefix=f"{settings.API_PREFIX}/calendars", tags=["Calendars"])



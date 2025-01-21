from portfolio.db.base_class import Base
# Importer tous les modèles ici
from portfolio.db.models.users import User
from portfolio.db.models.roles import Role
from portfolio.db.models.permissions import Permission
from portfolio.db.models.projects import Project
from portfolio.db.models.milestones import Milestone
from portfolio.db.models.missions import Mission
from portfolio.db.models.tags import Tag
from portfolio.db.models.technologies import Technology
from portfolio.db.models.pricing import Pricing
from portfolio.db.models.calendars import AvailabilityCalendar
from portfolio.db.models.feedbacks import UserFeedback
from portfolio.db.models.invoices import Invoice
from portfolio.db.models.invoices_infos import InvoiceInfo 
from portfolio.db.models.custom_blocks import CustomBlock
from portfolio.db.models.invoices_has_blocks import InvoiceHasCustomBlock
from portfolio.db.models.calendars import AvailabilityCalendar

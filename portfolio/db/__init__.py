from db.base_class import Base  # Assurez-vous que Base est défini dans base_class.py

# Importer tous les modèles ici
from db.models.users import User
from db.models.roles import Role
from db.models.permissions import Permission
from db.models.projects import Project
from db.models.milestones import Milestone
from db.models.missions import Mission
from db.models.tags import Tag
from db.models.technologies import Technology
from db.models.pricing import Pricing
from db.models.calendars import AvailabilityCalendar
from db.models.feedbacks import UserFeedback

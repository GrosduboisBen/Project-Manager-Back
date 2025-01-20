from sqlalchemy.orm import Session
from portfolio.db.models.roles import Role
from portfolio.schemas.roles import RoleCreate, RoleUpdate
from datetime import datetime

# Create a new role
def create_role(db: Session, role: RoleCreate):
    """
    Create a new role in the database.
    """
    db_role = Role(
        **role.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


# Get a single role by ID
def get_role(db: Session, role_id: str):
    """
    Retrieve a single role by its ID.
    """
    return db.query(Role).filter(Role.id == role_id).first()


# Get all roles with pagination
def get_roles_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of roles and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(Role).count()
    roles = db.query(Role).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "roles": roles,
    }


# Update a role
def update_role(db: Session, role_id: str, role: RoleUpdate):
    """
    Update an existing role by its ID.
    """
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        return None
    for key, value in role.model_dump(exclude_unset=True).items():
        setattr(db_role, key, value)
    db.commit()
    db.refresh(db_role)
    return db_role


# Delete a role
def delete_role(db: Session, role_id: str):
    """
    Delete a role by its ID.
    """
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        return None
    db.delete(db_role)
    db.commit()
    return db_role

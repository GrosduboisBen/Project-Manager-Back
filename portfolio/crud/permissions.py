from sqlalchemy.orm import Session
from portfolio.db.models.permissions import Permission
from portfolio.schemas.permissions import PermissionCreate, PermissionUpdate
from datetime import datetime

# Create a new permission
def create_permission(db: Session, permission: PermissionCreate):
    """
    Create a new permission in the database.
    """
    db_permission = Permission(
        **permission.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission


# Get a single permission by ID
def get_permission(db: Session, permission_id: str):
    """
    Retrieve a single permission by its ID.
    """
    return db.query(Permission).filter(Permission.id == permission_id).first()


# Get all permissions with pagination
def get_permissions_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of permissions and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(Permission).count()
    permissions = db.query(Permission).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "permissions": permissions,
    }


# Update a permission
def update_permission(db: Session, permission_id: str, permission: PermissionUpdate):
    """
    Update an existing permission by its ID.
    """
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not db_permission:
        return None
    for key, value in permission.model_dump(exclude_unset=True).items():
        setattr(db_permission, key, value)
    db.commit()
    db.refresh(db_permission)
    return db_permission


# Delete a permission
def delete_permission(db: Session, permission_id: str):
    """
    Delete a permission by its ID.
    """
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not db_permission:
        return None
    db.delete(db_permission)
    db.commit()
    return db_permission

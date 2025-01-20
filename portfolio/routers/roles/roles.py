from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.roles import (
    create_role,
    get_roles_with_count,
    get_role,
    update_role,
    delete_role,
)
from portfolio.schemas.roles import RoleCreate, RoleUpdate, RoleResponse, RoleListResponse

router = APIRouter()

@router.post("/", response_model=RoleResponse)
def create(role: RoleCreate, db: Session = Depends(get_db)):
    """
    Create a new role.
    """
    return create_role(db, role)


@router.get("/", response_model=RoleListResponse)
def read_roles(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of roles with pagination.
    """
    return get_roles_with_count(db, page=page, page_size=page_size)


@router.get("/{role_id}", response_model=RoleResponse)
def read_role(role_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a role by ID.
    """
    role = get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.put("/{role_id}", response_model=RoleResponse)
def update(role_id: str, role: RoleUpdate, db: Session = Depends(get_db)):
    """
    Update a role by ID.
    """
    updated_role = update_role(db, role_id, role)
    if not updated_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated_role


@router.delete("/{role_id}")
def delete(role_id: str, db: Session = Depends(get_db)):
    """
    Delete a role by ID.
    """
    deleted_role = delete_role(db, role_id)
    if not deleted_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted successfully"}

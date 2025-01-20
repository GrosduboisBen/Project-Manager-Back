from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.permissions import (
    create_permission,
    get_permissions_with_count,
    get_permission,
    update_permission,
    delete_permission,
)
from portfolio.schemas.permissions import PermissionCreate, PermissionUpdate, PermissionResponse, PermissionListResponse

router = APIRouter()

@router.post("/", response_model=PermissionResponse)
def create(permission: PermissionCreate, db: Session = Depends(get_db)):
    """
    Create a new permission.
    """
    return create_permission(db, permission)


@router.get("/", response_model=PermissionListResponse)
def read_permissions(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of permissions with pagination.
    """
    return get_permissions_with_count(db, page=page, page_size=page_size)


@router.get("/{permission_id}", response_model=PermissionResponse)
def read_permission(permission_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a permission by ID.
    """
    permission = get_permission(db, permission_id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission


@router.put("/{permission_id}", response_model=PermissionResponse)
def update(permission_id: str, permission: PermissionUpdate, db: Session = Depends(get_db)):
    """
    Update a permission by ID.
    """
    updated_permission = update_permission(db, permission_id, permission)
    if not updated_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return updated_permission


@router.delete("/{permission_id}")
def delete(permission_id: str, db: Session = Depends(get_db)):
    """
    Delete a permission by ID.
    """
    deleted_permission = delete_permission(db, permission_id)
    if not deleted_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return {"message": "Permission deleted successfully"}

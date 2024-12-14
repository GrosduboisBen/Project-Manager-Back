from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_missions():
    return {"message": "List of missions"}

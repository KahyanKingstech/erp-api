from fastapi import APIRouter

router = APIRouter()

@router.get("/api1")
def read_api1():
    return {"message": "This is API 1"}
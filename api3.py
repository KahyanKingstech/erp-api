from fastapi import APIRouter

router = APIRouter()

@router.get("/api3")
def read_api3():
    return {"message": "This is API 3"}

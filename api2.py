from fastapi import APIRouter

router = APIRouter()

@router.get("/api2")
def read_api2():
    return {"message": "This is API 2"}

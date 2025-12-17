from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to MyBackend!"}

@router.get("/status")
def get_status():
    return {"status": "ok"}
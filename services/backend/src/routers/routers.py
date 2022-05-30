from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"Health":"OK OK"}
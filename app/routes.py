from fastapi import APIRouter
from clothes.routes import router as clothes_router


router = APIRouter(prefix="/api")

router.include_router(clothes_router)

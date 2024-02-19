from fastapi import APIRouter
from controllers.movies_controllers import router as movies_router


router = APIRouter()
router.include_router(movies_router)

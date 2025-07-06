from fastapi import APIRouter
from starlette import status

from clothes.infrastructure.views.add_clothe import AddClothe

router = APIRouter(prefix="/clothes", tags=["clothes"])

router.add_api_route("/", endpoint=AddClothe().post, methods=["POST"], status_code=status.HTTP_201_CREATED)

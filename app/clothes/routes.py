from fastapi import APIRouter
from starlette import status

from clothes.infrastructure.views.add_clothe_view import AddClotheView

router = APIRouter(prefix="/clothes", tags=["clothes"])

router.add_api_route("/", endpoint=AddClotheView().post, methods=["POST"])

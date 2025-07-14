from starlette import status
from fastapi.responses import Response
from fastapi import UploadFile

from clothes.application.actions.async_create_clothe_action import CreateClotheActionParameters, AsyncCreateClotheAction
from clothes.application.adapters.fastapi_image_adapter import FastAPIImageAdapter
from clothes.infrastructure.clients.local_async_clothe_images_client import LocalAsyncClotheImagesClient
from clothes.infrastructure.repositories.sqlalchemy_async_clothes_repository import SQLAlchemyAsyncClothesRepository


class AddClotheView:
    async def post(self, image: UploadFile, response: Response):
        image_adapted = FastAPIImageAdapter(image=image)
        params = CreateClotheActionParameters(image=image_adapted)

        await AsyncCreateClotheAction(
            clothe_images_client=LocalAsyncClotheImagesClient(),
            clothes_repository=SQLAlchemyAsyncClothesRepository(),
        ).execute(params)

        response.status_code = status.HTTP_201_CREATED
        return

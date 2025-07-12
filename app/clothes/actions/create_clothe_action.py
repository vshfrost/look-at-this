from dataclasses import dataclass

from fastapi import UploadFile

from clothes.domain.clothe import Clothe
from clothes.domain.contracts.async_clothe_images_client import AsyncClotheImagesClient
from clothes.domain.contracts.async_clothes_repository import AsyncClothesRepository


@dataclass
class CreateClotheActionParameters:
    image: UploadFile

class CreateClotheAction:
    def __init__(self, clothes_repository: AsyncClothesRepository, clothe_images_client: AsyncClotheImagesClient):
        self._clothe_images_client = clothe_images_client
        self._clothes_repository = clothes_repository

    async def execute(self, params: CreateClotheActionParameters):
        clothe = Clothe.create()

        await self._clothe_images_client.upload(clothe, params.image.file)
        await self._clothes_repository.save(clothe)

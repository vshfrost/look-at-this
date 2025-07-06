from dataclasses import dataclass

from fastapi import UploadFile

from clothes.domain.clothe import Clothe
from clothes.domain.contracts.clothe_images_client import ClotheImagesClient
from clothes.domain.contracts.clothes_repository import ClothesRepository


@dataclass
class CreateClotheActionParameters:
    image: UploadFile

class CreateClotheAction:
    def __init__(self, clothes_repository: ClothesRepository, clothe_images_client: ClotheImagesClient):
        self._clothe_images_client = clothe_images_client
        self._clothes_repository = clothes_repository

    def execute(self, params: CreateClotheActionParameters):
        clothe = Clothe.create()

        self._clothe_images_client.upload(clothe, params.image.file)
        self._clothes_repository.save(clothe)

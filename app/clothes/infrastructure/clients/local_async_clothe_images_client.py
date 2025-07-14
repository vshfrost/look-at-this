import asyncio
import os

from PIL import Image

from clothes.domain.clothe import Clothe
from clothes.domain.contracts.async_clothe_images_client import AsyncClotheImagesClient
from clothes.domain.contracts.clothe_image_adapter import ClotheImageAdapter


class LocalAsyncClotheImagesClient(AsyncClotheImagesClient):
    async def upload(self, clothe: Clothe, image: ClotheImageAdapter) -> None:
        await asyncio.to_thread(self._process_and_upload, clothe=clothe, image=image)

    @staticmethod
    def _process_and_upload(clothe: Clothe, image: ClotheImageAdapter) -> None:
        image = Image.open(fp=image.file())
        image.thumbnail(size=(clothe.image.MAX_SIZE, clothe.image.MAX_SIZE))

        dir_name = os.path.dirname(clothe.image.file_path)
        os.makedirs(name=dir_name, exist_ok=True)
        image.save(
            fp=clothe.image.file_path,
            format=clothe.image.TYPE,
            quality=clothe.image.QUALITY
        )

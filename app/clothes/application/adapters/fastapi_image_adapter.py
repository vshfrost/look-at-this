from typing import BinaryIO

from fastapi import UploadFile

from clothes.domain.contracts.clothe_image_adapter import ClotheImageAdapter


class FastAPIImageAdapter(ClotheImageAdapter):
    def __init__(self, image: UploadFile):
        self._image = image

    def filename(self) -> str:
        return self._image.filename

    def content_type(self) -> str:
        return self._image.content_type

    def file(self) -> BinaryIO:
        return self._image.file

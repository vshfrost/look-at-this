import typing

from shared.domain.uuid import Uuid


class ClotheImage:
    PATH = "media/__name__.jpg"

    MAX_SIZE = 1024
    QUALITY = 85
    TYPE = "JPEG"

    def __init__(self, file_path: str):
        self._file_path = file_path

    @classmethod
    def create(cls, file_name: str) -> typing.Self:
        file_path = cls.PATH.replace("__name__", file_name)

        return cls(file_path=file_path)

    @property
    def file_path(self) -> str:
        return self._file_path

class Clothe:
    def __init__(self, id: Uuid, image: ClotheImage):
        self._id = id
        self._image = image

    @classmethod
    def create(cls) -> typing.Self:
        id = Uuid.create()
        image = ClotheImage.create(file_name=id.to_string())

        return cls(id=id, image=image)

    @property
    def image(self) -> ClotheImage:
        return self._image

    @property
    def id(self) -> Uuid:
        return self._id

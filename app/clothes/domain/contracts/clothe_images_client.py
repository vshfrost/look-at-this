import abc
from typing import BinaryIO

from clothes.domain.clothe import Clothe


class ClotheImagesClient(abc.ABC):
    @abc.abstractmethod
    def upload(self, clothe: Clothe, image: BinaryIO) -> None: ...

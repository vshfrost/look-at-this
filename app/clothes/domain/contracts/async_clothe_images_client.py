import abc
from typing import BinaryIO

from clothes.domain.clothe import Clothe


class AsyncClotheImagesClient(abc.ABC):
    @abc.abstractmethod
    async def upload(self, clothe: Clothe, image: BinaryIO) -> None: ...

import abc

from clothes.domain.clothe import Clothe
from clothes.domain.contracts.clothe_image_adapter import ClotheImageAdapter


class AsyncClotheImagesClient(abc.ABC):
    @abc.abstractmethod
    async def upload(self, clothe: Clothe, image: ClotheImageAdapter) -> None: ...

import abc

from clothes.domain.clothe import Clothe


class AsyncClothesRepository(abc.ABC):
    @abc.abstractmethod
    async def save(self, clothe: Clothe) -> None: ...

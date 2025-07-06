import abc

from clothes.domain.clothe import Clothe


class ClothesRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, clothe: Clothe) -> None: ...

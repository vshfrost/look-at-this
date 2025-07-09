from clothes.domain.clothe import Clothe
from clothes.domain.contracts.clothes_repository import ClothesRepository
from shared.infrastructure.models.clothes import Clothes
from shared.infrastructure.repositories.base_async_repository import BaseAsyncRepository


class SQLAlchemyAsyncClothesRepository(ClothesRepository, BaseAsyncRepository):
     async def save(self, clothe: Clothe) -> None:
        clothe_to_save = Clothes(
            id=clothe.id.value,
            file_path=clothe.image.file_path
        )

        self._session.add(clothe_to_save)
        await self._session.commit()

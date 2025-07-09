from unittest import mock
from uuid import UUID

import pytest
from _pytest.fixtures import fixture

from clothes.domain.clothe import Clothe, ClotheImage
from clothes.infrastructure.repositories.sqlalchemy_clothes_repository import SQLAlchemyClothesRepository
from shared.domain.uuid import Uuid


class TestClothesRepository:
    @fixture
    def mock_async_session(self):
        with mock.patch('sqlalchemy.ext.asyncio.AsyncSession') as mock_async_session:
            mock_async_session.commit = mock.AsyncMock()
            yield mock_async_session

    @pytest.mark.asyncio
    async def test_save_clothe_successfully(self, mock_async_session):
        clothe = Clothe(
            id=Uuid(UUID('123e4567-e89b-12d3-a456-426614174000')),
            image=ClotheImage(
                file_path='media/123e4567-e89b-12d3-a456-426614174000.jpg'
            )
        )

        await SQLAlchemyClothesRepository(session=mock_async_session).save(clothe)

        saved_clothe_model = mock_async_session.add.call_args[0][0]

        assert saved_clothe_model.id == UUID('123e4567-e89b-12d3-a456-426614174000')
        assert saved_clothe_model.file_path == 'media/123e4567-e89b-12d3-a456-426614174000.jpg'

        mock_async_session.add.assert_called_once()
        mock_async_session.commit.assert_awaited_once()

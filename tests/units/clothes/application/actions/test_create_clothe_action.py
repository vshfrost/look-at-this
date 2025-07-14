from typing import BinaryIO
from unittest import mock
from uuid import UUID

import pytest
from _pytest.fixtures import fixture
from fastapi import UploadFile

from clothes.application.actions.async_create_clothe_action import CreateClotheActionParameters, AsyncCreateClotheAction
from clothes.application.adapters.fastapi_image_adapter import FastAPIImageAdapter
from clothes.domain.contracts.async_clothe_images_client import AsyncClotheImagesClient
from clothes.domain.contracts.async_clothes_repository import AsyncClothesRepository


class TestCreateClotheAction:
    @fixture
    def mock_clothes_repository(self):
        return mock.create_autospec(AsyncClothesRepository, instance=True, spec_set=True)

    @fixture
    def mock_clothe_images_client(self):
        return mock.create_autospec(AsyncClotheImagesClient, instance=True, spec_set=True)

    @fixture
    def mock_id_generator(self):
        with mock.patch('shared.domain.uuid.uuid7') as mock_id_generator:
            yield mock_id_generator

    @pytest.mark.asyncio
    async def test_create_clothe_action(self, mock_clothes_repository, mock_clothe_images_client, mock_id_generator):
        mock_id_generator.return_value = UUID("123e4567-e89b-12d3-a456-426614174000")

        image = UploadFile(filename="image.jpg", file=BinaryIO())
        image_adapted = FastAPIImageAdapter(image=image)

        params = CreateClotheActionParameters(image=image_adapted)
        await AsyncCreateClotheAction(
            clothe_images_client=mock_clothe_images_client,
            clothes_repository=mock_clothes_repository,
        ).execute(params=params)

        saved_clothe = mock_clothes_repository.save.call_args[0][0]

        assert saved_clothe.image.file_path == "media/123e4567-e89b-12d3-a456-426614174000.jpg"

        mock_clothe_images_client.upload.assert_awaited_once()
        mock_clothes_repository.save.assert_awaited_once()

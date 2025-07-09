from typing import BinaryIO
from unittest import mock
from uuid import UUID

from _pytest.fixtures import fixture
from fastapi import UploadFile

from clothes.actions.create_clothe_action import CreateClotheActionParameters, CreateClotheAction
from clothes.domain.contracts.clothe_images_client import ClotheImagesClient
from clothes.domain.contracts.clothes_repository import ClothesRepository


class TestCreateClotheAction:
    @fixture
    def mock_clothes_repository(self):
        return mock.create_autospec(ClothesRepository, instance=True, spec_set=True)

    @fixture
    def mock_clothe_images_client(self):
        return mock.create_autospec(ClotheImagesClient, instance=True, spec_set=True)

    @fixture
    def mock_id_generator(self):
        with mock.patch('shared.domain.uuid.uuid7') as mock_id_generator:
            yield mock_id_generator

    def test_create_clothe_action(self, mock_clothes_repository, mock_clothe_images_client, mock_id_generator):
        mock_id_generator.return_value = UUID("123e4567-e89b-12d3-a456-426614174000")

        image = UploadFile(filename="image.jpg", file=BinaryIO())

        params = CreateClotheActionParameters(image=image)
        CreateClotheAction(
            clothe_images_client=mock_clothe_images_client,
            clothes_repository=mock_clothes_repository,
        ).execute(params=params)

        saved_clothe = mock_clothes_repository.save.call_args[0][0]

        assert saved_clothe.image.file_path == "media/123e4567-e89b-12d3-a456-426614174000.jpg"

        mock_clothe_images_client.upload.assert_called_once()
        mock_clothes_repository.save.assert_called_once()

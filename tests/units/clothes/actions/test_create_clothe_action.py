from typing import BinaryIO
from unittest.mock import create_autospec

from _pytest.fixtures import fixture
from fastapi import UploadFile

from clothes.actions.create_clothe_action import CreateClotheActionParameters, CreateClotheAction
from clothes.domain.contracts.clothe_images_client import ClotheImagesClient
from clothes.domain.contracts.clothes_repository import ClothesRepository


class TestCreateClotheAction:
    @fixture
    def mock_clothes_repository(self):
        return create_autospec(ClothesRepository)

    @fixture
    def mock_clothe_images_client(self):
        return create_autospec(ClotheImagesClient)

    def test_create_clothe_action(self, mock_clothes_repository, mock_clothe_images_client):
        image = UploadFile(filename="image.jpg", file=BinaryIO())

        params = CreateClotheActionParameters(image=image)
        CreateClotheAction(
            clothe_images_client=mock_clothe_images_client,
            clothes_repository=mock_clothes_repository,
        ).execute(params=params)

        mock_clothe_images_client.upload.assert_called_once()
        mock_clothes_repository.save.assert_called_once()

import typing
from typing import BinaryIO
from unittest import mock

import pytest
from _pytest.fixtures import fixture

from clothes.domain.clothe import Clothe, ClotheImage
from clothes.infrastructure.clients.local_async_clothe_images_client import LocalAsyncClotheImagesClient


class TestLocalAsyncClotheImagesClient:
    @fixture
    def mock_image_processor_open_call(self):
        with mock.patch('PIL.Image.open') as mock_image_processor_open_call:
            yield mock_image_processor_open_call

    @fixture
    def mock_os_makedirs_call(self):
        with mock.patch('os.makedirs') as mock_os_makedirs_call:
            yield mock_os_makedirs_call

    @pytest.mark.asyncio
    async def test_upload_image_when_format_is_jpg(
        self,
        mock_image_processor_open_call,
        mock_os_makedirs_call
    ):
        mock_image_to_process = mock.Mock()
        mock_image_processor_open_call.return_value = mock_image_to_process

        file = BinaryIO()
        clothe = Clothe(
            id=typing.Any,
            image=ClotheImage(
                file_path='media/123e4567-e89b-12d3-a456-426614174000.jpg'
            )
        )

        await LocalAsyncClotheImagesClient().upload(clothe=clothe, image=file)

        mock_image_to_process.thumbnail.assert_called_once_with(size=(1024, 1024))
        mock_image_to_process.save.assert_called_once_with(
            fp='media/123e4567-e89b-12d3-a456-426614174000.jpg',
            format='JPEG',
            quality=85,
        )
        mock_os_makedirs_call.assert_called_once_with(name='media', exist_ok=True)

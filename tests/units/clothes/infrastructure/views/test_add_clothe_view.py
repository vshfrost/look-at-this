from typing import BinaryIO
from unittest import mock

import pytest
from _pytest.fixtures import fixture
from fastapi import UploadFile
from fastapi.responses import Response

from clothes.application.actions.async_create_clothe_action import CreateClotheActionParameters
from clothes.infrastructure.views.add_clothe_view import AddClotheView


class TestAddClotheView:
    @fixture
    def mock_async_create_clothe_action(self):
        with mock.patch('clothes.application.actions.async_create_clothe_action.AsyncCreateClotheAction.execute') as mock_action:
            yield mock_action

    @pytest.mark.asyncio
    async def test_add_clothe_endpoint_calls_action_async(self, mock_async_create_clothe_action):
        uploaded_image = UploadFile(filename='test.jpg', file=BinaryIO())

        await AddClotheView().post(image=uploaded_image, response=Response())

        action_called_with = mock_async_create_clothe_action.call_args[0][0]
        assert isinstance(action_called_with, CreateClotheActionParameters)
        assert action_called_with.image.filename() == uploaded_image.filename

        mock_async_create_clothe_action.assert_awaited_once()

from typing import Dict
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock

from src.main import app
from src.schemas import CurrentChannelResponse, SourceOn

client = TestClient(app)


class TestAPISuccess():
    @patch('handlers.source_on_ps')
    async def test_source_on(self, mocked_source_on: AsyncMock) -> None:
        endpoint = "source_on/"
        input_data = SourceOn(
            channel=1,
            voltage=2,
            current=1,
        )
        expected_response = CurrentChannelResponse(
            output="ON",
            voltage=2,
            current=1,
            power=2
        )
        mocked_source_on.return_value = expected_response

        response = client.post(endpoint, json=input_data.model_dump())
        assert response.status_code == 200

        response_data = response.json()
        assert response_data == expected_response.model_dump()

    @patch('handlers.source_off_ps')
    async def test_source_off(self, mocked_source_off: AsyncMock) -> None:
        endpoint = "source_off/"
        input_data = {
            "channel": 1
        }
        expected_response = CurrentChannelResponse(
            output="OFF",
            voltage=2,
            current=1,
            power=2
        )
        mocked_source_off.return_value = expected_response

        response = client.post(endpoint, json=input_data)
        assert response.status_code == 200

        response_data = response.json()
        assert response_data == expected_response.model_dump()

    @patch('handlers.get_state_all_channels_ps')
    async def test_get_state_all(self, mocked_source_off: AsyncMock) -> None:
        endpoint = "get_state_all/"
        response = client.get(endpoint)
        assert response.status_code == 200
    
    @patch('handlers.get_state_current_channel_ps')
    async def test_get_state_current(self, mocked_source_off: AsyncMock) -> None:
        endpoint = "get_state_current/"
        input_data = {
            "channel": 1
        }
        expected_response = CurrentChannelResponse(
            output="OFF",
            voltage=2,
            current=1,
            power=2
        )
        mocked_source_off.return_value = expected_response

        response = client.post(endpoint, json=input_data)
        assert response.status_code == 200


class TestAPIErrors():
    async def test_value_out_of_range(self) -> None:
        endpoint = "source_on/"
        input_data = {
            "channel": 1,
            "voltage": 20,
            "current": 0,
        }

        response = client.post(endpoint, json=input_data)
        assert response.status_code == 422

        response_data: Dict = response.json()
        err_message = "Choose voltage in range 0~10(V)"
        assert response_data["detail"] == err_message

    async def test_invalid_value(self) -> None:
        endpoint = "source_on/"
        input_data = {
            "channel": 1,
            "voltage": "maxx",
            "current": 0,
        }

        response = client.post(endpoint, json=input_data)
        assert response.status_code == 422

        response_data: Dict = response.json()
        err_message = "Integers, floats and min/max available"
        assert response_data["detail"] == err_message

    async def test_channel_out_of_range(self) -> None:
        endpoint = "source_off/"

        response = client.post(endpoint, json={"channel": 4})
        assert response.status_code == 422

        response_data: Dict = response.json()
        assert response_data["detail"] == "Choose channel in range 0~3"

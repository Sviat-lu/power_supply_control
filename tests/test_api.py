from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock

from main import app
from src.schemas import CurrentChannelResponse, SourceOn

ROOT_ENDPOINT = "http://0.0.0.0:8000"


class TestAPISuccess:
    @patch(
        'src.controller.source_on_command',
        new_callable=AsyncMock,
    )
    async def test_source_on(self, mock_source_on_command: AsyncMock) -> None:
        client = TestClient(app)
        endpoint = f"{ROOT_ENDPOINT}/source_on/"

        input_data = SourceOn(
            channel=1,
            voltage=2,
            current=1,
        )

        expected_response = CurrentChannelResponse(
            output="OFF",
            voltage=2,
            current=1,
            power=2
        )

        mock_source_on_command.return_value = expected_response.model_dump()
        response = client.post(endpoint, json=input_data.model_dump())

        assert response.status_code == 200
        assert response.json() == expected_response.model_dump()
        mock_source_on_command.assert_called_once_with(input_data)

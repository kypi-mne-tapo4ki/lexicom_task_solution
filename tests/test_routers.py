import pytest
from fastapi import status
from httpx import AsyncClient

pytestmark = pytest.mark.anyio


async def test_check_data(client: AsyncClient) -> None:
    # Checking the missing number
    response = await client.get("/check_data", params={"phone": 89090000000})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Phone not found"}


async def test_write_data(client: AsyncClient) -> None:
    data = {"phone": "89090000000", "address": "ул. Ленина, д.86, кв. 56"}
    response = await client.post("/write_data", json=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == data

    # A repeated request with the same phone number should return an error
    response = await client.post("/write_data", json=data)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "already exists" in response.json()["detail"]


async def test_write_data_invalid_data(client: AsyncClient) -> None:
    # Send an invalid data
    invalid_data = {"phone": 8099999900, "address": "no address"}
    response = await client.post("/write_data", json=invalid_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

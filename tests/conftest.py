import pytest
from httpx import AsyncClient

from app.database import redis_client
from app.main import app


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client


@pytest.fixture(autouse=True)
async def flushdb():
    yield
    await redis_client.flushdb()

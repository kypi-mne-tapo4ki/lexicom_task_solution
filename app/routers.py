from fastapi import APIRouter, HTTPException, status
from app.models import Data

from app.database import redis_client

router = APIRouter()


@router.post("/write_data")
async def write_data(data: Data) -> Data:
    """Writing new data to the database."""
    if await redis_client.exists(data.phone):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Data for phone {data.phone} already exists",
        )

    await redis_client.set(data.phone, data.address)
    return data


@router.put("/write_data")
async def update_data(data: Data) -> Data:
    """Updating existing data in the database."""
    if not await redis_client.exists(data.phone):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Phone not found",
        )

    await redis_client.set(data.phone, data.address)
    return data


@router.get("/check_data")
async def check_data(phone: str) -> Data:
    """Checking for an entry in the database."""
    address = await redis_client.get(phone)
    if address is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Phone not found",
        )

    return Data(
        phone=phone,
        address=address,
    )

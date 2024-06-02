from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from schemas.product import ProductResponse
from services.product import get_product, list_products
from typing import List

router = APIRouter(prefix="/api/v1/products")


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product_endpoint(product_id: str, db: AsyncSession = Depends(get_session)):
    return await get_product(db, product_id)


@router.get("/", response_model=List[ProductResponse])
async def list_products_endpoint(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await list_products(db, skip, limit)

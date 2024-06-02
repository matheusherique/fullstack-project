from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models.product import Product
from sqlalchemy.future import select

async def get_product(db: AsyncSession, product_id: str):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

async def list_products(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Product).offset(skip).limit(limit))
    products = result.scalars().all()
    return products

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate
from db.redis import redis
import json

async def create_product(db: AsyncSession, product_create: ProductCreate):
    product = product_create.dict()
    new_product = Product(**product)
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    await redis.publish("product_updates", json.dumps({
        "status": "new",
        **product
    }))
    return new_product

async def update_product(
    db: AsyncSession,
    product_id: str,
    product_update: ProductUpdate
):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product_update.dict().items():
        setattr(product, key, value)
    await db.commit()
    await db.refresh(product)
    print(f'AQUI {product_update.dict()}', flush=True)
    await redis.publish("product_updates", json.dumps({
        "status": "update",
        "id": product_id,
        **product_update.dict()
    }))
    return product

async def delete_product(db: AsyncSession, product_id: str):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    await db.delete(product)
    await db.commit()
    await redis.publish("product_updates", json.dumps({
        "status": "deleted",
        "id": product_id
    }))
    return product

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate

async def create_product(db: AsyncSession, product_create: ProductCreate):
    new_product = Product(**product_create.dict())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
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
    return product

async def delete_product(db: AsyncSession, product_id: str):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    await db.delete(product)
    await db.commit()
    return {"detail": "Product deleted"}

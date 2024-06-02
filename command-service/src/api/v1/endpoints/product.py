from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from schemas.product import ProductCreate, ProductUpdate, ProductSchema
from services.product import create_product, update_product, delete_product

router = APIRouter(prefix="/api/v1/products")


@router.post("/", response_model=ProductSchema)
async def create_product_endpoint(
    product: ProductCreate, db: AsyncSession = Depends(get_session)
):
    return await create_product(db, product)


@router.put("/{product_id}", response_model=ProductSchema)
async def update_product_endpoint(
    product_id: str,
    product: ProductUpdate,
    db: AsyncSession = Depends(get_session)
):
    return await update_product(db, product_id, product)


@router.delete("/{product_id}", response_model=ProductSchema)
async def delete_product_endpoint(
    product_id: str, db: AsyncSession = Depends(get_session)
):
    return await delete_product(db, product_id)

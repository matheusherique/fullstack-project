from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1.endpoints import product
from db.base import Base
from db.session import engine
from db.redis import redis
from services.redis import subscribe_to_product_updates
import asyncio


app = FastAPI()

app.include_router(
    product.router,
    tags=["products"]
)


@app.on_event("startup")
async def startup():
    await redis.initialize()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    asyncio.create_task(subscribe_to_product_updates())


@app.on_event("shutdown")
async def shutdown():
    pass

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

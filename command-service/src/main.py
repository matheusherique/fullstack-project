from fastapi import FastAPI
from .api.v1.endpoints import product
from db.base import Base
from db.session import engine


app = FastAPI()

app.include_router(
    product.router,
    tags=["products"]
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    pass

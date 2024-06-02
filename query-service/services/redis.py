from db.redis import redis
from models.product import Product
from db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
import json


async def subscribe_to_product_updates():
    pubsub = redis.pubsub()
    await pubsub.subscribe("product_updates")
    async for message in pubsub.listen():
        if message['type'] == 'message':
            data = message['data']

            async for session in get_session():
                await __update_query_db(session, data)


async def __update_query_db(db: AsyncSession, payload: str):
    payload = json.loads(payload)
    status = payload.get('status')
    data = payload.get('data')

    if (status == "new"):
        new_product = Product(**data)
        db.add(new_product)
        await db.commit()
        await db.refresh(new_product)

    if (status == "update"):
        existing_product = await db.get(Product, data.get('id'))
        for key, value in data.items():
            setattr(existing_product, key, value)
        await db.commit()
        await db.refresh(existing_product)

    if (status == "deleted"):
        product = await db.get(Product, data.get('id'))
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        await db.delete(product)
        await db.commit()

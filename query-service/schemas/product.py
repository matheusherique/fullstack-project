from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: str
    name: str
    price: float
    quantity: int


class ProductResponse(BaseModel):
    id: str
    name: str
    price: float
    quantity: int

    class Config:
        from_attributes = True

from pydantic import BaseModel

class Product(BaseModel):
    name: str
    category_id: int
    supplier_id: int
    quantity: int
    unit_price: float
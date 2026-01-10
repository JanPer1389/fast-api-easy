from pydantic import BaseModel, Field

from typing import List, Optional

class CartItem(BaseModel):
    product_id: int = Field(..., description="The unique identifier of the product")
    quantity: int = Field(..., gt=0, description="The quantity of the product in the cart")

class CartItemCreate(CartItem):
    pass

class CartItemUpdate(BaseModel):
    quantity: int = Field(..., gt=0, description="The updated quantity of the product in the cart") 
    product_id: int 
    name: str = Field(..., description="Product name")
    price: float = Field(..., gt=0, description="Product price")
    subtotal: float = Field(..., description="Subtotal for the product (price * quantity)")
    image_url: Optional[str] = Field(None, description="URL of the product image")

class CartResponse(BaseModel):
    items: List[CartItem] = Field(..., description="List of items in the cart")
    items_count: int = Field(..., description="Total numbers of all items in the cart")
    total: float = Field(..., description="Total price of all items in the cart")

    class Config:
        from_attributes = True
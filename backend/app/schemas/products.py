from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., title="Product Name", max_length=100)
    description: Optional[str] = Field(None, title="Product Description", max_length=500)
    price: float = Field(..., gt=0, title="Product Price")
    category_id: int = Field(..., description="Category ID")
    image_url: Optional[str] = Field(None, description="Image URL")

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description="Unique Product ID")
    name: str 
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime 
    category: CategoryResponse = Field(..., description="Category Details")
    
    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description='Total number of products')


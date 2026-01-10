from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="The name of the category")
    slug: str = Field(..., min_length=5, max_length=100, 
                      description='A URL-friendly version of the category name')
    
class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description='Unique identifier for the category')
    
    class Config:
        from_attributes = True
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from ..models.products import Product
from ..schemas.products import ProductCreate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Product).options(joinedload(Product.category)).all()
   
    def get_by_id(self, product_id: int) -> Optional[Product]:
       return (self.db.query(Product).
               options(joinedload(Product.category)).
               filter(Product.id == product_id).
               all())
    
    
    def get_by_category_id(self, category_id: int) -> List[Product]:
        return (self.db.query(Product).
                options(joinedload(Product.category)).
                filter(Product.category_id == category_id).
                all()
                )
    
    def create(self, create_product: ProductCreate):
        db_product = Product(**create_product.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
    
    def get_multiple_by_ids(self, product_ids: List[int]) -> List[Product]:
        return (self.db.query(Product).
                options(joinedload(Product.category)).
                filter(Product.id.in_(product_ids)).
                all()
                )
    
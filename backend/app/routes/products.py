from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from ..database import get_db
from ..services.product_service import ProductService
from ..schemas.products import ProductResponse, ProductListResponse

router = APIRouter(
    prefix='/api/products',
    tags=['products']
)


@router.get('', response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()


@router.get('/{product_id}', response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_product_by_id(product_id=product_id)

@router.get('/category/{category_id}', response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_products_by_category(category_id=category_id)
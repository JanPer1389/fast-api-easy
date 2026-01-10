from sqlalchemy.orm import Session
from typing import List, Dict
from fastapi import APIRouter, Depends, status, HTTPException
from ..database import get_db
from ..services.product_service import ProductService
from ..schemas.products import ProductResponse
from ..services.cart_service import CartService, CartResponse, CartItemUpdate
from pydantic import BaseModel



router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)

class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int, int]  = {}

class UpdateCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int, int]  = {}

class RemoveFromCartRequest(BaseModel):
    product_id: int
    cart: Dict[int, int]  = {}

@router.post('add/', status_code = status.HTTP_200_OK)
def add_to_cart(request: AddToCartRequest,
                db: Session = Depends(get_db)):
    service = CartService(db)
    item = service.add_to_cart(request.cart, request.product_id, quantity = request.quantity)
    updated_cart = service.get_cart_details(request.cart, item)
    return {'cart': updated_cart}

@router.post('', response_model=CartResponse, status_code=status.HTTP_200_OK)
def update_cart(cart_data: UpdateCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    return service.get_cart_details(cart_data=cart_data)

@router.put('/update', status_code=status.HTTP_200_OK)
def update_cart_item(request: UpdateCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    item = CartItemUpdate(product_id=request.product_id, quantity=request.quantity)
    update_cart = service.update_cart_item(request.cart, item)
    return {'cart': update_cart}



@router.delete('/remove', status_code=status.HTTP_200_OK)
def remove_from_cart(request: RemoveFromCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    update_cart = service.remove_from_cart(request.cart, request.product_id)
    return {'cart': update_cart}
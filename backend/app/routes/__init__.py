from .products import router as products_router
from .cart import router as cart_router
from .categories import router as categories_router

__all__ = ['products_router', 'cart_router', 'categories_router']
from django.urls import path, include
from rest_framework import routers
from api.views.cart_view import CartViewSet, CartItemViewSet
from api.views.order_view import OrderViewSet, OrderItemViewSet
from api.views.payments_view import PaymentViewSet
from api.views.products_view import CategoryViewSet, ProductViewSet, ReviewViewSet
from api.views.users_view import UserViewSet, AddressViewSet

router = routers.DefaultRouter()
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers

from api.views import cart_view
from api.views import order_view
from api.views import payments_view
from api.views import products_view
from api.views import users_view


router = routers.DefaultRouter()
router.register(r'carts', cart_view.CartViewSet)
router.register(r'orders', order_view.OrderViewSet)
router.register(r'payments', payments_view.PaymentViewSet)
router.register(r'products', products_view.ProductViewSet)
router.register(r'users', users_view.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]





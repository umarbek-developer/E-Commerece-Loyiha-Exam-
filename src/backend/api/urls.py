from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views.cart_view import CartViewSet, CartItemViewSet
from api.views.order_view import OrderViewSet, OrderItemViewSet
from api.views.payments_view import PaymentViewSet
from api.views.products_view import CategoryViewSet, ProductViewSet, ReviewViewSet
from api.views.users_view import UserViewSet, AddressViewSet, UserRegistrationView

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
    # JWT Auth endpoints
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Router URLs
    path('', include(router.urls)),
]
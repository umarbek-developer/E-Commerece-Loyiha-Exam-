from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.cart_view import CartViewSet, CartItemViewSet
from api.views.order_view import OrderViewSet, OrderItemViewSet
from api.views.payments_view import PaymentViewSet
from api.views.products_view import (
    CategoryViewSet,
    ProductViewSet,
    ReviewViewSet,
    WishlistViewSet,
)
from api.views.users_view import UserViewSet, AddressViewSet, UserRegistrationView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response(
        {
            "register": "api/register/",
            "token": "api/token/",
            "token/refresh": "api/token/refresh/",
            "users": "api/users/",
            "addresses": "api/addresses/",
            "categories": "api/categories/",
            "products": "api/products/",
            "reviews": "api/reviews/",
            "carts": "api/carts/",
            "cart-items": "api/cart-items/",
            "orders": "api/orders/",
            "order-items": "api/order-items/",
            "payments": "api/payments/",
        }
    )


router = routers.DefaultRouter()
router.register(r"carts", CartViewSet)
router.register(r"cart-items", CartItemViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"order-items", OrderItemViewSet)
router.register(r"payments", PaymentViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"reviews", ReviewViewSet)
router.register(r"users", UserViewSet)
router.register(r"addresses", AddressViewSet)
router.register(r"wishlists", WishlistViewSet)

urlpatterns = [
    # JWT Auth endpoints
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Router URLs
    path("", include(router.urls)),
]

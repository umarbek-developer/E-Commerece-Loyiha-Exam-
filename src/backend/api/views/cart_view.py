from rest_framework.viewsets import ModelViewSet
from apps.cart.models import Cart, CartItem
from api.serializers.cart_serializer import CartSerializer, CartItemSerializer

# Create your views here.

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

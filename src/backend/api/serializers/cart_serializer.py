from rest_framework.serializers import ModelSerializer, ValidationError
from apps.cart.models import Cart, CartItem


class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"


class CartItemSerializer(ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"

    # validatsiyalar
    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError("Quantity must be at least 1.")
        return value
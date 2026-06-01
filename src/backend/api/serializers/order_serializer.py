from rest_framework.serializers import ModelSerializer, ValidationError
from apps.orders.models import Order, OrderItem


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

    def validate_status(self, value):
        allowed = ['pending', 'paid', 'shipped', 'delivered', 'cancelled']
        if value not in allowed:
            raise ValidationError(
                f"Status must be one of: {', '.join(allowed)}"
            )
        return value
    


class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"

    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError("Quantity must be at least 1.")
        return value

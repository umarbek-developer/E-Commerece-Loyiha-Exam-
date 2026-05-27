from rest_framework.viewsets import ModelViewSet
from apps.orders.models import Order, OrderItem
from api.serializers.order_serializer import OrderSerializer, OrderItemSerializer

# Create your views here.

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
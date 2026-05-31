from rest_framework.viewsets import ModelViewSet
from apps.payments.models import Payment
from api.serializers.payments_serializer import PaymentSerializer

# Create your views here.


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

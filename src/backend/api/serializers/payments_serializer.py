from rest_framework.serializers import ModelSerializer, ValidationError
from apps.payments.models import Payment


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"

    def validate_amount(self, value):
        if value <= 0:
            raise ValidationError("Amount must be greater than 0.")
        return value

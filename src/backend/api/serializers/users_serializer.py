from rest_framework.serializers import ModelSerializer
from apps.users.models import User, Address


class UserSerializer(ModelSerializer):

    class Meta:
        model = User  
        fields = '__all__'

class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address  
        fields = '__all__'



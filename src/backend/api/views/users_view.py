from rest_framework.viewsets import ModelViewSet
from apps.users.models import User, Address
from api.serializers.users_serializer import UserSerializer, AddressSerializer

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer



# products_view.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.products.models import Category, Product, Review, Wishlist
from apps.products.filters import ProductFilter
from api.serializers.products_serializer import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    WishlistSerializer,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Search by name and description
    search_fields = ["name", "description"]

    # Connect ProductFilter
    filterset_class = ProductFilter

    # Order by price, name, created_at
    ordering_fields = ["price", "name", "created_at"]
    ordering = ["created_at"]

    def get_permissions(self):
        # anyone can view products
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticatedOrReadOnly]
        # only admin can create, update, delete
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WishlistViewSet(ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    queryset = Wishlist.objects.all()

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import serializers
from apps.products.models import Category, Product, Review, Wishlist


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["user"]


class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField()
    discounted_price = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "discount",
            "discounted_price",  # calculated field
            "average_rating",  # calculated field
            "category",
            "image",
            "stock_quantity",
            "created_at",
            "updated_at",
        ]

    def validate_product(self, value):
        if value.stock_quantity <= 0:
            raise serializers.ValidationError("This product is out of stock.")
        return value

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
        read_only_fields = ["user"]

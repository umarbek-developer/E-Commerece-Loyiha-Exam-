import django_filters
from apps.products.models import Product

class ProductFilter(django_filters.FilterSet):
    # Filter by min price
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )
    # Filter by max price
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )
    # Filter by category
    category = django_filters.NumberFilter(
        field_name='category__id'
    )
    # Filter by min rating
    min_rating = django_filters.NumberFilter(
        field_name='reviews__rating',
        lookup_expr='gte'
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'min_price',
            'max_price',
            'min_rating'
        ]
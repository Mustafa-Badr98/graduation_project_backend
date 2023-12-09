from django_filters import FilterSet, RangeFilter
from .models import Property
from django_filters import rest_framework as filters


class PropertyFilter(FilterSet):
    class Meta:

        # area_size = RangeFilter()
        # number_of_bathrooms = RangeFilter()
        # number_of_bedrooms = RangeFilter()

        model = Property
        fields = {
            'price': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'area_size': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'location': ['exact', 'icontains'],
            'number_of_bathrooms': ['exact', 'icontains', 'lt', 'gt', 'gte', 'lte'],
            'number_of_bedrooms': ['exact', 'icontains', 'lt', 'gt', 'gte', 'lte'],
            'type': ['icontains',],
        }


class PropertySearchFilter(FilterSet):
    class Meta:

        # area_size = RangeFilter()
        # number_of_bathrooms = RangeFilter()
        # number_of_bedrooms = RangeFilter()

        model = Property
        fields = {
            'title': ['exact', 'icontains'],
            'id': ['exact', 'icontains'],
            'price': ['exact', 'icontains'],
            'location': ['exact', 'icontains'],
            'type': ['icontains',],
        }

from django_filters import FilterSet
from .models import NewUser


class UsersFilter(FilterSet):
    class Meta:

        

        model = NewUser
        fields = {
            'user_name': ['exact', 'icontains'],
            'id': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'mobile_phone': ['exact', 'icontains', ],
            'ratings': ['exact', 'icontains', 'lt', 'gt', 'gte', 'lte'],

        }

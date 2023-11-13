from rest_framework import serializers
from users.models import NewUser


class UserOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = (
            'id',
            'email',
            'user_name',
            'mobile_phone',

        )

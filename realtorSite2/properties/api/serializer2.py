from rest_framework import serializers
from properties.models import Property
from users.api.serializers2 import SellerSerializer


class PropertyModelSerializerGet(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

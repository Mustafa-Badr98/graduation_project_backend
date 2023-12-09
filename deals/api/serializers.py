
from rest_framework import serializers
from deals.models import Deal
from users.api.serializers3 import UserSerializer
from properties.api.serializers import PropertyModelSerializerPost


class DealSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    seller = UserSerializer(read_only=True)
    property = PropertyModelSerializerPost(read_only=True)

    class Meta:
        model = Deal
        fields = '__all__'

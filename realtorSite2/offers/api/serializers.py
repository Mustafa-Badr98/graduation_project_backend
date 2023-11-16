from rest_framework import serializers
from ..models import Offer
from users.api.serializers4 import UserOfferSerializer
from properties.api.serializer3 import PropertyModelSerializerOffer


class OfferSerializer(serializers.ModelSerializer):
    user = UserOfferSerializer(read_only=True)
    property = PropertyModelSerializerOffer()

    class Meta:
        model = Offer
        fields = '__all__'

from rest_framework import serializers
from ..models import Offer
from users.api.serializers4 import UserOfferSerializer


class OfferSerializer(serializers.ModelSerializer):
    user = UserOfferSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'

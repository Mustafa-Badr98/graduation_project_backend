
from rest_framework import serializers
from ratings.models import Rating
from users.api.serializers4 import UserOfferSerializer


class RatingSerializer(serializers.ModelSerializer):
    user = UserOfferSerializer(read_only=True)
    rated_by=UserOfferSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = '__all__'

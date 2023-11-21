
from rest_framework import serializers
from ratings.models import Rating



class RatingSerializer(serializers.ModelSerializer):
    # user=
    class Meta:
        model = Rating
        fields = '__all__'

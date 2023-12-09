
from rest_framework import serializers
from users.models import NewUser
from properties.api.serializers import FavoritePropertyModelSerializer
from django.db.models import Avg


class UserSerializer(serializers.ModelSerializer):

    favorites = FavoritePropertyModelSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    num_ratings = serializers.SerializerMethodField()

    class Meta:
        model = NewUser
        fields = (
            'id',
            'favorites',
            'avg_rating',
            'num_ratings',
            'password',
            'email',
            'user_name',
            'first_name',
            'last_name',
            'mobile_phone',
            'profile_pic',
        )

    def get_avg_rating(self, obj):
        avg_rating = obj.ratings.aggregate(Avg('rating'))['rating__avg']
        return avg_rating

    def get_num_ratings(self, obj):
        num_ratings = obj.ratings.count()
        return num_ratings


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = (
            'id',
            'email',
            'user_name',
            'mobile_phone',
            'profile_pic',

        )



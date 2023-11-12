from django.forms import ValidationError
from rest_framework import serializers
from users.models import NewUser
from rest_framework import validators
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
# from favorites.api.serializers import FavoriteSerializer
from properties.api.serializers import FavoritePropertyModelSerializer, PropertyModelSerializerPost
from deals.api.serializers import DealSerializer
from ratings.api.serializers import RatingSerializer
from django.db.models import Avg
from comments.api.serializers import CommentSerializer

# UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'

    def create(self, clean_data):
        user_obj = NewUser.objects.create_user(
            email=clean_data['email'], password=clean_data['password'], user_name=clean_data['user_name'])
        user_obj.mobile_phone = clean_data['mobile_phone']
        user_obj.location = clean_data['location']
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(
            username=clean_data['email'], password=clean_data['password'])
        if not user:
            return 0

        return user


class UserSerializer(serializers.ModelSerializer):
    favorites = FavoritePropertyModelSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    num_ratings = serializers.SerializerMethodField()
    properties_owned = PropertyModelSerializerPost(
        many=True, read_only=True, source='propertiesForSeller')
    deals_sold = DealSerializer(many=True, read_only=True, source='DealSeller')
    deals_bought = DealSerializer(
        many=True, read_only=True, source='DealBuyer')

    comments = CommentSerializer(
        many=True, read_only=True, source="comments_on_user",)

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
            'properties_owned',
            'deals_sold',
            'deals_bought',
            'comments',
        )

    def get_avg_rating(self, obj):
        avg_rating = obj.ratings.aggregate(Avg('rating'))['rating__avg']
        return avg_rating

    def get_num_ratings(self, obj):
        num_ratings = obj.ratings.count()
        return num_ratings

    # id = serializers.IntegerField(read_only=True)
    # email = serializers.EmailField(max_length=100)
    # user_name = serializers.CharField(max_length=200,required=False)
    # first_name=serializers.CharField(required=False)
    # last_name = serializers.CharField(required=False)
    # mobile_phone=serializers.IntegerField(required=False)
    # profile_pic= serializers.ImageField(required=False)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     return  NewUser.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data['title']
    #     instance.description = validated_data['description']
    #     instance.area_size=validated_data['area_size']
    #     instance.price = validated_data['price']
    #     instance.location = validated_data['location']
    #     instance.number_of_bedrooms = validated_data['number_of_bedrooms']
    #     instance.number_of_bathrooms = validated_data['number_of_bathrooms']
    #     instance.image = validated_data['image']
    #     instance.lat = validated_data['lat']
    #     instance.lon = validated_data['lon']
    #     instance.save()
    #     return  instance

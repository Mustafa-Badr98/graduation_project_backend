from rest_framework import serializers
from properties.models import Property,PropertyImage
from users.api.serializers2 import SellerSerializer
from rest_framework import serializers



class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image']


class PropertyModelSerializerGet(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'




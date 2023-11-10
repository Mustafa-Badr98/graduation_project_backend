from rest_framework import serializers
from properties.models import Property
from properties.api.serializer2 import PropertyImageSerializer
from offers.api.serializers import OfferSerializer 
# from users.api.serializers3 import UserSerializer

# from rest_framework import validators


class PropertySerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200,required=False)
    area_size=serializers.IntegerField(required=False)
    price = serializers.FloatField(default=0)
    location=serializers.CharField(max_length=100,required=False)
    lat=serializers.FloatField(required=False)
    lon=serializers.FloatField(required=False)    
    number_of_bedrooms=serializers.IntegerField(required=False)
    number_of_bathrooms=serializers.IntegerField(required=False)
    image= serializers.ImageField(required=False)  
    
    
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    offers = OfferSerializer(many=True, read_only=True)



    def create(self, validated_data):
        print(validated_data)
        return  Property.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.area_size=validated_data['area_size']
        instance.price = validated_data['price']
        instance.location = validated_data['location']
        instance.number_of_bedrooms = validated_data['number_of_bedrooms']
        instance.number_of_bathrooms = validated_data['number_of_bathrooms']
        instance.image = validated_data['image']
        instance.lat = validated_data['lat']
        instance.lon = validated_data['lon']
        instance.save()
        return  instance
    

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['offers'] = OfferSerializer(instance.offers.all(), many=True).data
        return representation
    
    
    
class PropertyModelSerializerPost(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'   
    
    
class FavoritePropertyModelSerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Property
        fields = '__all__'       
    
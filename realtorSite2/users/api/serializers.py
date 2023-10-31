


from rest_framework import serializers
from users.models import NewUser
# from rest_framework import validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = NewUser
        fields = '__all__'
    
    
    
    
    
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
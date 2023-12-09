from rest_framework import serializers
from properties.models import Property,PropertyImage
from rest_framework import serializers



class PropertyModelSerializerOffer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'




from users.models import NewUser
from rest_framework import serializers
      
class SellerSerializer(serializers.ModelSerializer):  
       class Meta:

        model = NewUser
        fields = '__all__'        


   
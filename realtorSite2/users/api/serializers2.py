from users.models import NewUser
from rest_framework import serializers
      
class SellerSerializer(serializers.ModelSerializer):  
       class Meta:

        model = NewUser
        fields = (
            'id',
            'email',
            'user_name',
            'mobile_phone',
            'profile_pic',
            'is_admin',
        )     


   
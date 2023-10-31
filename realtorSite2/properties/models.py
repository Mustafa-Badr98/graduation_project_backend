from django.db import models
from users.models import NewUser
# Create your models here.

class Properties(models.Model):
    
    title=models.CharField(max_length=50,null=False)
    description=models.CharField(max_length=200,null=True,blank=True)
    area_size=models.IntegerField(null=True)
    price=models.FloatField(max_length=100,null=False)
    location=models.CharField(max_length=50,null=True)
    lat=models.FloatField(null=True)
    lon=models.FloatField(null=True)
    number_of_bedrooms=models.IntegerField(null=True)
    number_of_bathrooms=models.IntegerField(null=True)
    image=models.ImageField(upload_to='accounts/properties/images/', max_length=None,null=True,blank=True)
    seller=models.ForeignKey(NewUser, verbose_name=("Seller User"), on_delete=models.CASCADE,null=True, blank=True
                              ,related_name='seller')
    
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f'{self.title} BY {self.seller.user_name}'
    
    @classmethod
    def get_all_properties(cls):
        return cls.objects.all()
    
    
    @classmethod
    def get_specific_property(cls, id):
        return cls.objects.filter(id=id).first()
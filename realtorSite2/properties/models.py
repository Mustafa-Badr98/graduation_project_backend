from django.db import models
from users.models import NewUser
# Create your models here.


class Property(models.Model):

    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=1200, null=True, blank=True)
    area_size = models.IntegerField(null=True)
    price = models.FloatField(max_length=100, null=False)
    location = models.CharField(max_length=50, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    type = models.CharField(null=True)
    number_of_bedrooms = models.IntegerField(null=True)
    number_of_bathrooms = models.IntegerField(null=True)
    image = models.ImageField(
        upload_to='accounts/properties/images/', max_length=None, null=True, blank=True)
    seller = models.ForeignKey('users.NewUser', verbose_name=(
        "Seller User"), on_delete=models.CASCADE, null=True, blank=True, related_name='propertiesForSeller')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    offers = models.ManyToManyField(
        'offers.Offer', blank=True, null=True, related_name='property_offers')

    STATE_CHOICES = [
        ('live', 'Live'),
        ('sold', 'Sold'),
    ]

    state = models.CharField(
        max_length=4,
        choices=STATE_CHOICES,
        default='live',  # Set the default state to 'live'
    )

    def __str__(self):
        return f'{self.title} BY {self.seller}'

    @classmethod
    def get_all_properties(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_property(cls, id):
        return cls.objects.filter(id=id).first()

    @classmethod
    def get_live_properties(cls):
        return cls.objects.filter(state='live').order_by('-created_at')

    @classmethod
    def get_sold_properties(cls):
        return cls.objects.filter(state='sold')


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='accounts/properties/images/', null=True, blank=True)

    def __str__(self):
        return f'Image for {self.property.title}'

    class Meta:
        verbose_name_plural = 'Property Images'

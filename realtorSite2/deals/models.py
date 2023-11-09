from django.db import models

# Create your models here.


class Deal(models.Model):
    seller = models.ForeignKey(
        'users.NewUser', on_delete=models.CASCADE, null=True, blank=True, related_name='DealSeller')
    buyer = models.ForeignKey(
        'users.NewUser', on_delete=models.CASCADE, null=True, blank=True, related_name='DealBuyer')
    property = models.ForeignKey(
        'properties.Property', on_delete=models.CASCADE, related_name='propertySold', null=True, blank=True)
    price = models.FloatField(max_length=100, null=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Deal Done between {self.seller} and {self.buyer} agreed on price {self.price}'

    @classmethod
    def get_all_deals(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_deal(cls, id):
        return cls.objects.filter(id=id).first()

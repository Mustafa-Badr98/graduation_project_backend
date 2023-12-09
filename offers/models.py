from django.db import models
from users.models import NewUser
from properties.models import Property


class Offer(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name="offer_owner")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="offer_property")
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Offer by {self.user} on {self.property}'
    
    @classmethod
    def get_all_offers(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_offer(cls, id):
        return cls.objects.filter(id=id).first()


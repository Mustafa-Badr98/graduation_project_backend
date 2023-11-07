from django.db import models
from users.models import NewUser
from properties.models import Property
# Create your models here.


class Favorite(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE,null=True)
    favorite = models.ForeignKey(Property, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f'{self.user.email} favorite {self.favorite}'


    class Meta:
        # Enforce unique constraint on user and favorite together
        unique_together = ['user', 'favorite']

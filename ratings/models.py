from django.db import models

# Create your models here.
from users.models import NewUser
from django.db.models import Avg



class Rating(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(
        NewUser, related_name="ratings_given", on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def get_user_average_rate(self):
        user = self.user
        average_rating = Rating.objects.filter(
            user=user).aggregate(Avg('rating'))['rating__avg']
        return average_rating

    def __str__(self):
        return '{} rated {} {}'.format(self.rated_by.user_name, self.user.user_name, self.rating)

    class Meta:
       
        unique_together = ['user', 'rated_by']
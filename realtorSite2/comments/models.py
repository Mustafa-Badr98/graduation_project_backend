from django.db import models
from users.models import NewUser
# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(
        NewUser, related_name='comments_on_user', on_delete=models.CASCADE)
    commented_by = models.ForeignKey(
        NewUser, related_name='comments_given_by_user', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} commented on {}\'s profile'.format(self.commented_by.user_name, self.user.user_name)

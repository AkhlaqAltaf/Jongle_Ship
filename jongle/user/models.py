
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    actions_required = models.CharField(
        max_length=20, choices=[('none', 'None'), ('forward', 'Forward'), ('reconsolidate', 'Reconsolidate')],
        default='none'
    )

    def __str__(self):
        return self.user.username

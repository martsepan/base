from django.db import models

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Додайте поля за необхідності, наприклад:
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # date_of_birth = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username


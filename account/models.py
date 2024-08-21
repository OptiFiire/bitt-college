from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
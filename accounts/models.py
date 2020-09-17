from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    required_fields = ['username']

    def __str__(self):
        return f"{self.username}"

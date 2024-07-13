from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    phone_number = models.CharField(max_length=225, null=True, blank=True, db_index=True, unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.get_full_name()}"

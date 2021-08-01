from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    last_seen = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Kullanici'
        verbose_name_plural = 'Kullanicilar'

    def __str__(self):
        return self.username

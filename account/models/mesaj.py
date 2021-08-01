from django.db import models
from account.models import CustomUserModel

class MesajModel(models.Model):
    gonderen = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="mesajlar")
    alan = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="mesajlarim")
    mesaj = models.TextField()

    class Meta:
        db_table = 'Mesajlar'
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'
        

    def __str__(self):
        return self.alan.username
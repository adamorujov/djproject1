from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel
from blog.models.abstract_models import DateAbstractModel

class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()

    class Meta:
        db_table = "yorum"
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"

    def __str__(self):
        return self.yazan.username
    
class Cevaplar(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='cevap')
    yorum = models.ForeignKey(YorumModel, on_delete=models.CASCADE, related_name='cevaplar')
    cevap = models.TextField()

    class Meta:
        db_table = "cevap"
        verbose_name = "Cevap"
        verbose_name_plural = "Cevaplar"

    def __str__(self):
        return self.yazan.username


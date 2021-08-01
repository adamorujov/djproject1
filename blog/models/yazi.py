from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.models.abstract_models import DateAbstractModel

class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to='yazi_resimleri')
    detay_resim = models.ImageField(upload_to='yazi_resimleri', default="")
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from='baslik', unique=True)
    bakis_sayi = models.IntegerField(default=0)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yazilar')

    class Meta:
        db_table="Yazi"
        verbose_name='Yazi'
        verbose_name_plural='Yazilar'

    def __str__(self):
        return self.baslik
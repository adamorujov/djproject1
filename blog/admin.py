from django.contrib import admin
from blog.models import KategoriModel, YazilarModel

# Register your models here.
admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    list_display = (
        'baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi', 'yazar',
    )



admin.site.register(YazilarModel, YazilarAdmin)

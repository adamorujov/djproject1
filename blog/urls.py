from django.urls import path
from .views import iletisim, anasayfa, kategori, yazilarim, detay

urlpatterns = [
    path('', anasayfa.anasayfa, name='anasayfa'),
    path('iletisim/', iletisim.iletisim, name='iletisim'),
    path('kategori/<slug:KategoriSlug>', kategori.kategori, name="kategori"),
    path('yazilarim/', yazilarim.yazilarim, name="yazilarim"),
    path('detay/<slug:slug>', detay.detay, name="detay"),
]
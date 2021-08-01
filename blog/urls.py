from django.urls import path
from .views import iletisim, anasayfa, kategori, yazilarim, detay, mesajiletildi, yazi_ekle, send_maill, yazi_guncelle, yazi_sil, yorum_sil
from django.views.generic import TemplateView

urlpatterns = [
    path('', anasayfa.anasayfa, name='anasayfa'),
    path('iletisim/', iletisim.IletisimFormView.as_view(), name='iletisim'),
    path('kategori/<slug:KategoriSlug>', kategori.KategoriListView.as_view(), name="kategori"),
    path('yazilarim/', yazilarim.yazilarim, name="yazilarim"),
    path('detay/<slug:slug>', detay.DetayView.as_view(), name="detay"),
    path('iletisim/mesajiletildi', mesajiletildi.mesajiletildi, name='mesajiletildi'),
    path('yazi-ekle/', yazi_ekle.YaziEkleCreateView.as_view(), name='yaziekle'),
    path('send-mail/', send_maill.send_maill, name='sendmail'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle.YaziGuncelleUpdateView.as_view(), name='yaziguncelle'),
    path('yazi-sil/<slug:slug>/', yazi_sil.yazi_sil, name='yazisil'),
    path('yorum-sil/<int:id>/', yorum_sil.yorum_sil, name='yorumsil'),
    path('yazi-sil-onay/<slug:slug>', yazi_sil.YaziSilDeleteView.as_view(), name='yazisilonay'),
    path('konu-okuma/', TemplateView.as_view(template_name='pages/konu_okuma.html'), name='konuokuma'),
]
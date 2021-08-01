from django.urls import path
from .views import cikis, sifre_degistir, profil_guncelle, kayit, giris, hesab_ziyaret_et, users_list, mesajlar

app_name='account'
urlpatterns = [
    path('cikis/', cikis.cikis, name='cikis'),
    path('sifre-degistir/', sifre_degistir.sifre_degistir, name='sifredegistir'),
    path('profil-guncelle/', profil_guncelle.profil_guncelle, name='profilguncelle'),
    path('kayit/', kayit.kayit, name='kayit'),
    path('giris/', giris.giris, name='giris'),
    path('userslist/', users_list.UserListView.as_view(), name='userslist'),
    path('<str:username>/', hesab_ziyaret_et.HesabZiyaretDetailView.as_view(), name='hesabziyaretet'),
    path('mesajlar', mesajlar.MesajlarListView.as_view(), name='mesajlar'),
]

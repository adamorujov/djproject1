from django.urls import path
from .views import iletisim, anasayfa

urlpatterns = [
    path('', anasayfa.anasayfa),
    path('iletisim/', iletisim.iletisim),
]
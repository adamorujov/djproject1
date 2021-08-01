from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, YorumModel
from account.models import CustomUserModel
from django.views.generic import DetailView

class HesabZiyaretDetailView(DetailView):
    template_name = "pages/hesab-ziyaret-et.html"
    context_object_name = 'kullanici'

    def get_object(self):
        kullanici = get_object_or_404(CustomUserModel, username=self.kwargs['username'])
        return kullanici

    def yorum_sayi(self):
        yorum_sayi = 0
        for yazi in self.get_object().yazilar.all():
            yorum_sayi += len(yazi.yorumlar.all())
        return yorum_sayi

    def bakis_sayi(self):
        bakis_sayi = 0
        for yazi in self.get_object().yazilar.all():
            bakis_sayi += yazi.bakis_sayi
        return bakis_sayi
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["yazilar"] = self.get_object().yazilar.order_by('-id')
        context["postsayi"] = len(self.get_object().yazilar.all())
        context["yorumsayi"] = self.yorum_sayi()
        context["bakissayi"] = self.bakis_sayi()
        return context
    


def hesab_ziyaret_et(request, username):
    kullanici = get_object_or_404(CustomUserModel, username=username)
    kullanici_yorumlari = 0
    bakis_sayi = 0
    for yazi in kullanici.yazilar.all():
        kullanici_yorumlari += len(yazi.yorumlar.all())
        bakis_sayi += yazi.bakis_sayi
    
    context = {
        'kullanici' : kullanici,
        'yazilar' : kullanici.yazilar.order_by('-id'),
        'postsayi' : len(kullanici.yazilar.all()),
        'yorumsayi' : kullanici_yorumlari,
        'bakissayi' : bakis_sayi,
    }

    return render(request, 'pages/hesab-ziyaret-et.html', context)
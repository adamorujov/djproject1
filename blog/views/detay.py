from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from blog.models import YazilarModel, YorumModel
from blog.forms import YorumEkleModelForm, yorum_ekle
from django.views import View
import logging

logger = logging.getLogger('konu_okuma')

class DetayView(View):
    http_method_names = ['get', 'post']
    yorum_ekle_form = YorumEkleModelForm

    def get(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        logger.info('konu okundu: ' + request.user.username + " " + yazi.baslik )
        yorumlar = yazi.yorumlar.order_by('-id').filter(parent=None)
        yazi.bakis_sayi +=1
        yazi.save()

        context = {
            'yazi' : yazi,
            'yorumlar' : yorumlar,
            'yorum_sayi' : len(yazi.yorumlar.all()),
            'yorum_ekle_form' : self.yorum_ekle_form,
        }

        return render(request, 'pages/detay.html', context)

    def post(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorum_ekle_form = self.yorum_ekle_form(request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            if request.POST.get('answer') != 'A':
                yorum.parent = get_object_or_404(YorumModel, id=request.POST.get('answer'))
            yorum.save()
            return redirect('detay', slug=yazi.slug)


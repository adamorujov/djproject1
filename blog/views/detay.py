from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import YazilarModel, YorumModel, Cevaplar

def detay(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug)
    yorumlar = yazi.yorumlar.order_by('-id')
    context = {
        "yazi" : yazi,
        "yorumlar" : yorumlar,
        "yorum_sayi" : len(yorumlar),
    }

    return render(request, 'pages/detay.html', context)
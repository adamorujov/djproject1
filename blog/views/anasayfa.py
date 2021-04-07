from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator
from django.db.models import Q

def anasayfa(request):
    yazilar = YazilarModel.objects.order_by('-id')
    sorgu = request.GET.get('sorgu')

    netice = -1

    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains=sorgu) |
            Q(icerik__icontains=sorgu)
        )
        netice = len(yazilar)

    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 1)
    context = {
        'yazilar' : paginator.get_page(sayfa),
        'netice' : netice,
        'sorgu' : sorgu,
    }
    return render(request, 'pages/anasayfa.html', context)
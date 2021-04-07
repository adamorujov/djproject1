from django.shortcuts import render, get_object_or_404
from blog.models import KategoriModel
from django.core.paginator import Paginator

def kategori(request, KategoriSlug):
    kategori = get_object_or_404(KategoriModel, slug=KategoriSlug)
    yazilar = kategori.yazi.order_by("-id")

    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 1)

    context = {
        'yazilar' : paginator.get_page(sayfa),
        'kategori' : kategori,
    }

    return render(request, 'pages/kategori.html', context)

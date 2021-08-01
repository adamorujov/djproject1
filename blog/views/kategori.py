from django.shortcuts import render, get_object_or_404
from blog.models import KategoriModel
from django.core.paginator import Paginator
from django.views.generic import ListView

class KategoriListView(ListView):
    template_name = 'pages/kategori.html'
    context_object_name = 'yazilar'
    paginate_by = 3

    def get_queryset(self):
        kategori = get_object_or_404(KategoriModel, slug=self.kwargs['KategoriSlug'])
        return kategori.yazi.order_by('-id')

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

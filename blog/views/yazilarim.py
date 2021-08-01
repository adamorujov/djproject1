from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import YazilarModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='blog/')
def yazilarim(request):
    yazilarim = request.user.yazilar.order_by('-id')

    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilarim, 1)

    context = {
        'yazilarim' : paginator.get_page(sayfa),
    }

    return render(request, 'pages/yazilarim.html', context)
    
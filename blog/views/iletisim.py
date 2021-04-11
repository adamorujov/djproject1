from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from blog.models import IletisimModel
from blog.forms import IletisimForm1

def iletisim(request):
    form = IletisimForm1()

    if request.method == 'POST':
        form = IletisimForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anasayfa')
        else:
            form = IletisimForm1()
    
    context = {
        'form' : form,
    }
    return render(request, 'pages/iletisim.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import KayitFormu
from django.contrib.auth import login, authenticate

def kayit(request):
    form = KayitFormu(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('anasayfa')
    else:
        form = KayitFormu()
    
    context = {
        'form' : form,
    }

    return render(request, 'pages/kayit.html', context)
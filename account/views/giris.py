from django.shortcuts import render, redirect, get_object_or_404
from account.forms import GirisFormu
from account.models import CustomUserModel
from django.contrib.auth import authenticate, login
from django.contrib import messages

def giris(request):
    form = GirisFormu(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #user = get_object_or_404(CustomUserModel, username=username, password=password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('anasayfa')
        else:
            messages.error(request, 'Uye bulunamadi')
    
    context = {
        'form' : form,
    }

    return render(request, 'pages/uye-girisi.html', context)
        

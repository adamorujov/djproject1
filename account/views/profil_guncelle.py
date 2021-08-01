from django.shortcuts import render, redirect
from account.forms import ProfilGuncellemeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/')
def profil_guncelle(request):
    form = ProfilGuncellemeForm(request.POST or None, files=request.FILES or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profil Guncellendi')
    else:
        form = ProfilGuncellemeForm(instance=request.user)

    context = {
        'form' : form,
    }
    
    return render(request, 'pages/profil-guncelle.html', context)

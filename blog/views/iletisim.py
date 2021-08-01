from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from blog.models import IletisimModel
from blog.forms import IletisimForm1
from django.contrib import messages
from django.views import View
from django.views.generic import FormView

class IletisimFormView(FormView):
    template_name = "pages/iletisim.html"
    form_class = IletisimForm1
    success_url = '/iletisim/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class IletisimView(View):
    http_method_names = ['get', 'post']
    form = IletisimForm1

    def get(self, request):
        context = {
            'form' : self.form,
        }
        return render(request, 'pages/iletisim.html', context)

    def post(self, request):
        form = IletisimForm1(request.POST)
        form.save()
        messages.success(request, 'Mesaj gonderildi')
        return redirect('iletisim')


def iletisim(request):
    form = IletisimForm1()

    if request.method == 'POST':
        form = IletisimForm1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesaj gonderildi')

    form = IletisimForm1()
    
    context = {
        'form' : form,
    }
    return render(request, 'pages/iletisim.html', context)
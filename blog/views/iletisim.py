from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def iletisim(request):
    return render(request, 'pages/iletisim.html')
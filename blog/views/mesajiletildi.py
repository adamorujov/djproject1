from django.shortcuts import render

def mesajiletildi(request):
    mesajiletildi = "Mesajiniz iletildi"
    context = {
        'mesajiletildi' : mesajiletildi,
    }
    return render(request, 'pages/mesajiletildi.html', context)
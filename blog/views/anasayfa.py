from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim' : 'Orucov Adem',
    }
    return render(request, 'pages/anasayfa.html', context)
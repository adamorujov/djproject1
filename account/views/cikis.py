from django.shortcuts import redirect
from django.contrib.auth import logout
from django.utils import timezone

def cikis(request):
    request.user.last_seen = timezone.now()
    request.user.save()
    logout(request)
    return redirect("anasayfa")
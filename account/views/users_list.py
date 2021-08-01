from django.views.generic import ListView
from account.models import CustomUserModel
from django.shortcuts import render, redirect

class UserListView(ListView):
    model = CustomUserModel
    template_name = 'pages/users-list.html'
    
    
    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["kullanicilar"] = CustomUserModel.objects.all()
        return context"""
    
        
def users_list(request):
    kullanicilar = CustomUserModel.objects.all()

    return render(request, 'pages/users-list.html', context={
        'kullanicilar' : kullanicilar,
    })
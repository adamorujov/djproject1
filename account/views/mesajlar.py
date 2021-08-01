from django.views.generic import ListView
from account.models import MesajModel, CustomUserModel

class MesajlarListView(ListView):
    template_name = 'pages/mesajlar.html'
    context_object_name = 'mesajlar'

    def get_queryset(self):
        queryset = MesajModel.objects.order_by('-id').filter(alan=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mesajsayi"] = len(self.get_queryset())
        return context
    

from django.shortcuts import redirect, get_object_or_404
from blog.models import YazilarModel
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class YaziSilDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('account:giris')
    template_name = "pages/yazi-sil-onay.html"
    success_url = reverse_lazy('yazilarim')

    def get_queryset(self):
        yazi = YazilarModel.objects.filter(slug=self.kwargs['slug'], yazar=self.request.user)
        return yazi

@login_required(login_url='/')
def yazi_sil(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug, yazar=request.user)
    yazi.delete()
    return redirect('/')
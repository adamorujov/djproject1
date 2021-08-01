from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from account.models import CustomUserModel

class ProfilGuncellemeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUserModel
        fields = ('avatar', 'email', 'first_name', 'last_name')
from django import template
from account.models import CustomUserModel

register = template.Library()

@register.simple_tag
def users_list():
    users = CustomUserModel.objects.all()
    return users
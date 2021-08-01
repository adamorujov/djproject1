from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel, MesajModel

# Register your models here.

class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Degistirme Alani', {
            'fields': ['avatar',]
        }),
    )

admin.site.register(CustomUserModel, CustomAdmin)

@admin.register(MesajModel)
class MesajAdmin(admin.ModelAdmin):
    list_display = ('alan', 'gonderen', 'mesaj')
    search_fields = ('alan', 'gonderen')
    


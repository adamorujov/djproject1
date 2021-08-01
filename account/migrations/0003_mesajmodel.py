# Generated by Django 3.1.5 on 2021-07-28 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customusermodel_last_seen'),
    ]

    operations = [
        migrations.CreateModel(
            name='MesajModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesaj', models.TextField()),
                ('alan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alan', to=settings.AUTH_USER_MODEL)),
                ('gonderen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gonderen', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
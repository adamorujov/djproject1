# Generated by Django 3.1.5 on 2021-04-07 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_yazilarmodel_detay_resim'),
    ]

    operations = [
        migrations.AddField(
            model_name='yorummodel',
            name='cevaplar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anayorum', to='blog.yorummodel'),
        ),
    ]

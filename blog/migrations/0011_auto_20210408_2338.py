# Generated by Django 3.1.5 on 2021-04-08 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210407_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cevaplar',
            name='yorum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cevaplar', to='blog.yorummodel'),
        ),
    ]
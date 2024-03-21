# Generated by Django 4.2.7 on 2024-01-06 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0003_alter_item_item_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='for_user',
            field=models.CharField(default='RestOwner', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='prod_code',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

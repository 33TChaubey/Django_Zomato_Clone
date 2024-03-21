# Generated by Django 4.2.7 on 2024-01-13 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0006_item_rest_owner_alter_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='added_by',
            field=models.CharField(default='user', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='rest_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

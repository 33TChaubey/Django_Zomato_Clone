# Generated by Django 4.2.7 on 2024-01-06 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_item_for_user_item_prod_code_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='for_user',
        ),
    ]

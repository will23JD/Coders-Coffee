# Generated by Django 3.2 on 2022-08-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_wishlist_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
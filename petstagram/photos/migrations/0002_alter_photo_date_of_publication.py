# Generated by Django 5.1.1 on 2024-09-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_of_publication',
            field=models.DateField(auto_now_add=True),
        ),
    ]

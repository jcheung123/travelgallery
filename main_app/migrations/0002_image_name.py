# Generated by Django 4.0.3 on 2022-04-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='new image', max_length=200),
        ),
    ]

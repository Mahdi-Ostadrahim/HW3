# Generated by Django 3.2.15 on 2022-09-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20220927_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='counted_view',
            field=models.IntegerField(default=0),
        ),
    ]

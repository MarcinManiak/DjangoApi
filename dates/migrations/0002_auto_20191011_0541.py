# Generated by Django 2.2.6 on 2019-10-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dates',
            name='date_of_modifiation',
        ),
        migrations.AddField(
            model_name='dates',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

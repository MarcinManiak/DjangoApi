# Generated by Django 2.2.6 on 2019-10-11 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_auto_20191011_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dates',
            name='updated_at',
        ),
    ]

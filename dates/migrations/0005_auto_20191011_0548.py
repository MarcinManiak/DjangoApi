# Generated by Django 2.2.6 on 2019-10-11 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0004_dates_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dates',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
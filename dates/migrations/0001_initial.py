# Generated by Django 2.2.6 on 2019-10-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('date_of_modifiation', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-14 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKalos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('profesion', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_link', models.CharField(max_length=300)),
                ('cl_link', models.CharField(max_length=600)),
            ],
        ),
    ]

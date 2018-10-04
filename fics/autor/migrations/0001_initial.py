# Generated by Django 2.1.2 on 2018-10-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('usuario', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('data_inscricao', models.DateField(auto_now_add=True)),
                ('descricao', models.TextField(max_length=255)),
            ],
        ),
    ]

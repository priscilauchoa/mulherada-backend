# Generated by Django 2.1.7 on 2019-03-21 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=2000)),
                ('contato', models.CharField(max_length=250)),
            ],
        ),
    ]

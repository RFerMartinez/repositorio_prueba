# Generated by Django 3.1 on 2021-12-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

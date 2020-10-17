# Generated by Django 2.2.12 on 2020-10-17 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50, null=True)),
                ('nome_completo', models.CharField(max_length=50, null=True)),
                ('cpf', models.CharField(max_length=14, null=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(null=True)),
                ('telefone', models.CharField(max_length=16, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

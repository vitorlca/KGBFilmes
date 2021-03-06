# Generated by Django 2.2.12 on 2020-12-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileUpload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='image',
            name='ano_producao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='classificacao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='diretor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='genero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='pais_de_origem',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

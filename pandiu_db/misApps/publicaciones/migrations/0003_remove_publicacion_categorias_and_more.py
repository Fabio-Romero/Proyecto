# Generated by Django 5.0.9 on 2024-10-22 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_publicacion_archivo_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='categorias',
        ),
        migrations.RemoveField(
            model_name='publicacioncategoria',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='publicacioncategoria',
            name='publicacion',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='PublicacionCategoria',
        ),
    ]

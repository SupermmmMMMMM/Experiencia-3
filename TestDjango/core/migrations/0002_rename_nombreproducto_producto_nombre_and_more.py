# Generated by Django 5.0.6 on 2024-06-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombreProducto',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
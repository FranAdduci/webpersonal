# Generated by Django 4.1.2 on 2023-01-26 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portafolio',
            name='rol',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='imagen',
            field=models.ImageField(upload_to='portafolio'),
        ),
    ]
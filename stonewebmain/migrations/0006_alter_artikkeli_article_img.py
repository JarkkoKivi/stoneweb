# Generated by Django 4.0.6 on 2022-07-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stonewebmain', '0005_remove_artikkeli_artikkelin_teksti_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikkeli',
            name='Article_img',
            field=models.FileField(blank=True, default='', null=True, upload_to='coding-images/'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stonewebmain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikkeli',
            name='Article_img',
            field=models.FileField(default='', upload_to=''),
        ),
    ]

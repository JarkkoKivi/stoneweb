# Generated by Django 4.0.6 on 2022-07-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stonewebmain', '0006_alter_artikkeli_article_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikkeli',
            name='article_slug',
            field=models.SlugField(null=True),
        ),
    ]

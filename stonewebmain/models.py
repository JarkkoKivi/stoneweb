from django.db import models
from datetime import date
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Artikkeli(models.Model):
    article_id = models.AutoField(primary_key=True)
    pub_date = models.DateField(auto_now_add=True)
    article_title = models.CharField(max_length=50, name='Artikkelin_otsikko')
    slug = models.SlugField(null=True, unique=False)
    article_tech = models.CharField(max_length=50, default='', name='koodikielet')
    article_text = RichTextField(blank=True, null=True)
    article_img = models.FileField(name='Article_img', default='', blank=True, null=True, upload_to='coding-images/')

    def __str__(self):
        return f"{self.Artikkelin_otsikko} | {date.strftime(self.pub_date, '%d.%m.%Y')}"

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug}) 

    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.Artikkelin_otsikko)
    #     return super().save(*args, **kwargs)
    
class Sivun_tiedot(models.Model):
    logo = models.FileField(name='Logo')
    header_bg = models.FileField(name='Header Background')
    page_main_title = models.CharField(max_length=50, name='Main title')
    page_subtitle = models.CharField(max_length=200, name='Subtitle')
    page_description = models.TextField(name='Page description')

    

    

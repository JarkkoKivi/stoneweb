from django.contrib import admin
MAX_OBJECTS = 1
# Register your models here.
from stonewebmain.models import Artikkeli, Sivun_tiedot

class SivunTiedotAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

# Rekisteröi artikkeli
@admin.register(Artikkeli)
class ArtikkeliAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Artikkelin_otsikko',),} #automaattinen slug otsikosta

admin.site.register(Sivun_tiedot, SivunTiedotAdmin)



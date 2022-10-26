from django.shortcuts import render
from django.http import HttpResponse
from stonewebmain.models import Artikkeli, Sivun_tiedot
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class index(TemplateView):
    model = Sivun_tiedot
    template_name = 'main/front_page.html'
    

def site_form(request):
    return render(request, 'forms/site_properties.html', {} )

class Koodaukset(ListView):
    model = Artikkeli
    template_name = "main/koodausprojektit.html"

class KoodauksetDetail(DetailView):
    model = Artikkeli
    template_name = "main/koodaus-page.html" 



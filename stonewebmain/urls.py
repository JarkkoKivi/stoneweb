from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name = 'home'),
    path('settings/', views.site_form, name = 'settings'),
    path('koodaukset/', views.Koodaukset.as_view(), name='koodauslista'),
    path('koodaukset/<slug:slug>/', views.KoodauksetDetail.as_view(), name='article_detail'),

]

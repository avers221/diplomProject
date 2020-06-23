from django.urls import path
from . import views

app_name = 'about_company'

urlpatterns = [
    path('', views.company_information, name='company_information')
]
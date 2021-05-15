from django.urls import path
from Thesaurus_API import views

urlpatterns = [
    path('', views.main, name='home'),
]

from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.forms, name='forms'),
    path('results/', views.results, name='results'),
    path('visualizardados/', views.viewdata, name='visualizardados'),

]
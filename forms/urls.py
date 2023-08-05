from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.forms, name='forms'),
    path('results/', views.results, name='results'),
    path('report/', views.report, name='results'),
    path('adicionarPergunta/', views.adicionarPergunta, name='adicionarPergunta'),
    path('<int:id_forms>', views.report, name='report' )
]
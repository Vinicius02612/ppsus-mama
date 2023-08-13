 
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from forms.api import viewsets as FormViewSet

router = routers.DefaultRouter()

router.register(r'insertForms', FormViewSet.FormViewSet, basename='Formulario')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('forms/', include('forms.urls')),
    path('api-quest/', include(router.urls))
]

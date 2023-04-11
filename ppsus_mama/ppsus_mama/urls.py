 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('forms/', include('forms.urls')),
    path('forms/results', include('forms.urls')),

    path('account/', include('account.urls'))
]

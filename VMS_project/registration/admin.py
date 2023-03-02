from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('path/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]


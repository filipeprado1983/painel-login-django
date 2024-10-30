from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('painel_login.urls')),  # Incluindo o app painel_login
]

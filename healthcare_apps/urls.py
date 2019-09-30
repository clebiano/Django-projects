"""healthcare_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from home import urls as home_urls
from patients import urls as patients_urls
from patients.api.viewsets import PatientViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PatientViewSet, base_name='healthcare_apps')

urlpatterns = [
    path('', include(home_urls)),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('pacientes/', include(patients_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

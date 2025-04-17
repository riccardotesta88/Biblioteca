"""
URL configuration for Biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from os.path import basename

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from Biblioteca import settings
import gestione.views as vi
from django.views.generic.base import TemplateView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'getlibri', vi.LibriViewGet,basename='getlibri')
router.register(r'setlibro', vi.LibriViewSet,basename="setlibro")
router.register(r'setautore', vi.AutoreViewSet,basename="setautore")
router.register(r'seteditore', vi.EditoreViewSet,basename="seteditore")

urlpatterns = (([
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new

    # Gestione percorsi per la gestione dei libri che rimanda al modulo gestione\urls.py
    path('', include('gestione.urls')),
    # API
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/',include(router.urls)),
]
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))



urlpatterns += staticfiles_urlpatterns()
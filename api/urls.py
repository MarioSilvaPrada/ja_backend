"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from settings.views import SettingsAPIView
from projects.views import ProjectAPIView, SingleProjectAPIView
from about.views import AboutAPIView
from partners.views import PartnersAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/settings/', SettingsAPIView.as_view(), name='settings'),
    path('api/projects/', ProjectAPIView.as_view(), name='projects'),
    path('api/projects/<int:pk>/', SingleProjectAPIView.as_view(), name='single project'),
    path('api/about/', AboutAPIView.as_view(), name='about'),
    path('api/partners/', PartnersAPIView.as_view(), name='partners'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

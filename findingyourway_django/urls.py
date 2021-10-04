"""findingyourway_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from findingyourway import views
from findingyourway.views import AdventureList, PathList, RouteList, EndingList

router = DefaultRouter()
router.register(r'adventure', views.AdventureList, 'adventure')
router.register(r'path', views.PathList, 'path')
router.register(r'route', views.RouteList, 'route')
router.register(r'ending', views.EndingList, 'ending')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path("", include("findingyourway.urls")),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

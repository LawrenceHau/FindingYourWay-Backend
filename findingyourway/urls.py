
from django.urls import path
from . import views
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("adventures/", views.AdventureList.as_view(), name="adventure_list"),
    path("adventures/<int:pk>", views.AdventureDetail.as_view(), name="adventure_detail"),
    path("paths/", views.PathList.as_view(), name="path_list"),
    path("paths/<int:pk>", views.PathDetail.as_view(), name="path_detail"),
    path("routes/", views.RouteList.as_view(), name="route_list"),
    path("routes/<int:pk>", views.RouteDetail.as_view(), name="route_detail"),
    path("endings", views.EndingList.as_view(), name="ending_list"),
    path("endings/<int:pk>", views.EndingDetail.as_view(), name="ending_detail"),
    ]
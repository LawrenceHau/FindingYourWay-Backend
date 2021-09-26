
from django.urls import path
from . import views
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("adventures/", views.AdventureList.as_view(), name="adventure_list"),
    path("adventures/<int:pk>", views.AdventureDetail.as_view(), name="adventure_detail"),
    path("paths/", views.PathList.as_view(), name="path_list"),
    path("paths/<int:pk>", views.PathDetail.as_view(), name="path_detail"),
    path("routetableone/", views.RouteTableOneList.as_view(), name="routetableone_list"),
    path("routetableone/<int:pk>", views.RouteTableOneDetail.as_view(), name="routetableone_detail"),
    path("routetabletwo/", views.RouteTableTwoList.as_view(), name="routetabletwo_list"),
    path("routetabletwo/<int:pk>", views.RouteTableTwoDetail.as_view(), name="routetabletwo_detail"),
    path("routetablethree/", views.RouteTableThreeList.as_view(), name="routetablethree_list"),
    path("routetablethree/<int:pk>", views.RouteTableThreeDetail.as_view(), name="routetablethree_detail"),
    path("goodending/", views.GoodEndingList.as_view(), name="goodending_list"),
    path("goodending/<int:pk>", views.GoodEndingDetail.as_view(), name="goodending_detail"),
    path("badending/", views.BadEndingList.as_view(), name="badending_list"),
    path("badending/<int:pk>", views.BadEndingDetail.as_view(), name="badending_detail"),
    path("neutralending/", views.NeutralEndingList.as_view(), name="neutralending_list"),
    path("neutralending/<int:pk>", views.NeutralEndingDetail.as_view(), name="neutralending_detail"),
    ]
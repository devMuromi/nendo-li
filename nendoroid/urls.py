from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("nendoroids/", views.NendoroidList.as_view()),
    path("nendoroids/<str:number>", views.NendoroidDetail.as_view()),
    path("series/", views.SeriesList.as_view()),
    path("series/<int:pk>", views.SeriesDetail.as_view()),
    path("manufacturers/", views.ManufacturerList.as_view()),
    path("manufacturers/<int:pk>", views.ManufacturerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

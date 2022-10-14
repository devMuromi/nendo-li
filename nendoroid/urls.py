from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('nendoroid/', views.nendoroid_list),
    path('nendoroid/<int:pk>', views.nendoroid_detail),

    path('series/', views.SeriesList.as_view()),
    path('series/<int:pk>', views.SeriesDetail.as_view()),

    path('manufacturer/', views.ManufacturerList.as_view()),
    path('manufacturer/<int:pk>', views.ManufacturerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
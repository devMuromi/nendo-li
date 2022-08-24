from django.urls import path

from . import views

urlpatterns = [
    path('', views.nendoroid_list),
    path('<int:pk>', views.nendoroid_detail),
]
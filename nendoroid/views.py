from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from nendo_li import permissions as customPermissions
from nendoroid.models import Nendoroid, Series, Manufacturer
from nendoroid.serializers import (
    NendoroidSerializer,
    SeriesSerializer,
    ManufacturerSerializer,
)

# Nendoroid
class NendoroidList(generics.ListCreateAPIView):
    queryset = Nendoroid.objects.all()
    serializer_class = NendoroidSerializer
    permission_classes = [customPermissions.ReadOnly]

    # numbering query string 인식, 기본값: 000
    def get_queryset(self):
        q = self.request.query_params.get("numbering", "")
        qs = super().get_queryset()
        if q:
            qs = qs.filter(numbering=q)
        else:
            qs = qs.filter(numbering="000")
        return qs

    filter_backends = [OrderingFilter]
    ordering_fields = ["number"]
    ordering = ["number"]


class NendoroidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nendoroid.objects.all()
    serializer_class = NendoroidSerializer
    permission_classes = [customPermissions.ReadOnly]

    lookup_field = "number"


# Series
class SeriesPagination(PageNumberPagination):
    page_size = 50
    # page_size_query_param = "page_size"
    # max_page_size = 100


class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    pagination_class = SeriesPagination
    permission_classes = [customPermissions.ReadOnly]


class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [customPermissions.ReadOnly]


# Manufacturer
class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [customPermissions.ReadOnly]


class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [customPermissions.ReadOnly]

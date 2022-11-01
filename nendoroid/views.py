from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from nendoroid.models import Nendoroid, Series, Manufacturer
from nendoroid.serializers import NendoroidSerializer ,SeriesSerializer, ManufacturerSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.filters import OrderingFilter

class NendoroidList(generics.ListCreateAPIView):
    queryset = Nendoroid.objects.all()
    serializer_class = NendoroidSerializer

    # numbering query string 인식, 기본값: 000
    def get_queryset(self):
        q = self.request.query_params.get('numbering', '')
        qs = super().get_queryset()
        if q:
            qs = qs.filter(numbering=q)
        else:
            qs = qs.filter(numbering='000')
        return qs

    filter_backends = [OrderingFilter]
    ordering_fields = ['number']
    ordering = ['number']

class NendoroidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nendoroid.objects.all()
    serializer_class = NendoroidSerializer

    lookup_field = 'number'

# @api_view(['GET', 'POST'])
# def nendoroid_list(request, format=None):
#     if request.method == 'GET':
#         nendoroids = Nendoroid.objects.all()
#         serializer = NendoroidSerializer(nendoroids, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = NendoroidSerializer(data=request.data)            
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def nendoroid_detail(request, pk, format=None):
#     try:
#         nendoroid = Nendoroid.objects.get(pk=pk)
#     except Nendoroid.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = NendoroidSerializer(nendoroid)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = NendoroidSerializer(nendoroid, data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         nendoroid.delete()
#         return Response(status=204)


# Series
class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

# Manufacturer
class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

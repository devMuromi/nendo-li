from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from nendoroid.models import Nendoroid
from nendoroid.serializers import NendoroidSerializer

# def index(request):
#     return HttpResponse("NENDO DB")

@csrf_exempt
def nendoroid_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        nendoroids = Nendoroid.objects.all()
        serializer = NendoroidSerializer(nendoroids, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NendoroidSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def nendoroid_detail(request, pk):
    try:
        nendoroid = Nendoroid.objects.get(pk=pk)
    except Nendoroid.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NendoroidSerializer(nendoroid)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NendoroidSerializer(nendoroid, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        nendoroid.delete()
        return HttpResponse(status=204)

# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from rest_framework import permissions
# from nendoroid.serializers import UserSerializer, GroupSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
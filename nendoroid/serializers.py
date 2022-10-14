from django.contrib.auth.models import User, Group
from rest_framework import serializers

from nendoroid.models import Manufacturer, Nendoroid, Series


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class NendoroidSerializer(serializers.Serializer):
#     class Meta:
#         model = Nendoroid
#         fields = ['number', 'name_ko', 'name_en', 'name_ja', 'series', 'manufacturer', 'sculptor', 'gsc_number', 'release_date', 'gender']

class NendoroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nendoroid
        fields = "__all__"
        
class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = "__all__"
        
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"

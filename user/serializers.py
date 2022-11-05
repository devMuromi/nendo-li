import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nendo_li.settings")

# from django.contrib.auth.models import User, Group
from user.models import User
from rest_framework import serializers

from nendoroid.models import Manufacturer, Nendoroid, Series


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ["url", "name"]

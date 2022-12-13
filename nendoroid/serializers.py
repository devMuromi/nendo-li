import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nendo_li.settings")

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from nendoroid.models import Manufacturer, Nendoroid, Series


class NendoroidSerializer(serializers.ModelSerializer):
    # release_date = serializers.JSONField(allow_null=True)
    class Meta:
        model = Nendoroid
        fields = "__all__"


class SeriesSerializer(serializers.ModelSerializer):
    nendoroid_set = NendoroidSerializer(many=True, read_only=True)

    class Meta:
        model = Series
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"

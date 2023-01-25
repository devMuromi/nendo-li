import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nendo_li.settings")
from user.models import User
from rest_framework import serializers
from nendoroid.serializers import NendoroidSerializer, NendoroidPhotoSerializer


class UserSerializer(serializers.ModelSerializer):
    nendoroidphoto_set = NendoroidPhotoSerializer(many=True, read_only=True)
    # nendoroid_owned = NendoroidSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "nendoroidphoto_set",
            "is_superuser",
            "is_staff",
            "email",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

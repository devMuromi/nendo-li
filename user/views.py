from rest_framework import generics
from user.models import User
from nendoroid.models import NendoroidPhoto
from user.serializers import UserSerializer
from nendoroid.serializers import NendoroidPhotoSerializer
from rest_framework import permissions
from nendo_li import permissions as customPermissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyPage(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# class UserNendoroidPhoto(generics.ListAPIView):
#     queryset = NendoroidPhoto.objects.all()
#     serializer_class = NendoroidPhotoSerializer
#     permission_classes = [permissions.IsAuthenticated]

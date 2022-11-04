from rest_framework import viewsets, status, generics, permissions
from rest_framework.permissions import AllowAny
from .models import Users
from .serializers import UserSerializers, SelectUserSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]

    def destroy(self, request, pk=None):
        item = get_object_or_404(Users, name=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserList(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = Users.objects.all()
#     serializer_class = SelectUserSerializers        
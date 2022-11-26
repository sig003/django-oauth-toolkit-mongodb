from rest_framework import viewsets, status, generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .models import Users, Houses
from .serializers import UserSerializers, SelectUserSerializers, HouseSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = 'name'

    # def update(self, request, pk=None):
    #     print(pk)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk=None):
    #     item = get_object_or_404(Users, name=pk)
    #     item.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# class UserList(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = Users.objects.all()
#     serializer_class = SelectUserSerializers        

class HousesViewSet(viewsets.ModelViewSet):
    queryset = Houses.objects.all()
    serializer_class = HouseSerializers
    #permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
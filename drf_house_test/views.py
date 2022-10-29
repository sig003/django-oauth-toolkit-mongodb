from rest_framework import viewsets, status, generics, permissions
from rest_framework.permissions import AllowAny
from .models import Users
from .serializers import InsertUserSerializers, SelectUserSerializers
from rest_framework.response import Response

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = InsertUserSerializers
    permission_classes = [AllowAny]

    # def list(self, request):
    #     print(request.data)
    #     return Response({'status': 'select ok'}, status=status.HTTP_200_OK)

# class UserList(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = Users.objects.all()
#     serializer_class = SelectUserSerializers        
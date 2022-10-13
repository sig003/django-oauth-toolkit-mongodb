from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsAuthenticatedOrCreate
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
#from django.db.models import Q

class RegisterView(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.filter(is_admin__in=[False])
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

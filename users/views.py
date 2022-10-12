from .models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from .permissions import IsAuthenticatedOrCreate

class RegisterView(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
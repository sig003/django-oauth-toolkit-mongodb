from rest_framework import viewsets, status, generics, permissions
from rest_framework.permissions import AllowAny
from .models import Users
from .serializers import InsertUserSerializers, SelectUserSerializers
import pymongo
from rest_framework.response import Response



class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = InsertUserSerializers
    permission_classes = [AllowAny]

    # Use pymongo 
    # def create(self, request):
    #     email = request.data['email']
    #     name = request.data['name']
    #     house = request.data['house']

    #     data = {
    #         "email": email,
    #         "name": name,
    #         "house": house
    #     }
    #     collection.insert_one(data)
    #     return Response({'status': 'insert ok'}, status=status.HTTP_201_CREATED)

    # def update(self, request, pk=None):
    #     house = request.data['house']

    #     collection.update_one({"name":"test5"}, {"$set":{"house":house}})
    #     return Response({'status': 'update ok'}, status=status.HTTP_200_OK)


    # def list(self, request):
    #     print(request.data)        
    #     print(11)
    #     queryset = Users.objects.all()
    #     serializer_class = SelectUserSerializers
    #     print(queryset)
    #     return Response({'status': 'select ok'}, status=status.HTTP_200_OK)

    def list(self, request):
        results = collection.find()
        for result in results:
            print (result)
        return Response({'status': 'select ok'}, status=status.HTTP_200_OK)

class UserList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Users.objects.all()
    serializer_class = SelectUserSerializers        
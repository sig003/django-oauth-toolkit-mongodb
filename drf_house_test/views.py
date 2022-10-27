from rest_framework import viewsets, status, generics, permissions
from rest_framework.permissions import AllowAny
from .models import Users
from .serializers import InsertUserSerializers, SelectUserSerializers
import pymongo
from rest_framework.response import Response
import os, json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse

BASE_DIR = Path(__file__).resolve().parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

MONGODB_HOST_FILE = get_secret("MONGODB_HOST")

client = pymongo.MongoClient(MONGODB_HOST_FILE)
dbname = client['test_db']
collection = dbname['drf_users']

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
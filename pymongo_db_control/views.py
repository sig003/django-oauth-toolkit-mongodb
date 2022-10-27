from rest_framework import viewsets, status
import pymongo
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# import os, json
# from pathlib import Path
# from django.core.exceptions import ImproperlyConfigured
from bson import json_util
from core.views import *

MONGODB_HOST_FILE = getMongoDBConnectHostFile()

# BASE_DIR = Path(__file__).resolve().parent.parent

# secret_file = os.path.join(BASE_DIR, 'secrets.json')
# with open(secret_file) as f:
#     secrets = json.loads(f.read())

# def get_secret(setting):
#     try:
#         return secrets[setting]
#     except KeyError:
#         error_msg = "Set the {} environment variable".format(setting)
#         raise ImproperlyConfigured(error_msg)

# MONGODB_HOST_FILE = get_secret("MONGODB_HOST")

client = pymongo.MongoClient(MONGODB_HOST_FILE)
dbname = client['test_db']
collection = dbname['drf_users']

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        requestEmail = request.data.get('email')
        requestName = request.data.get('name')

        reqData = {}
        if requestEmail != None:
            reqData['email'] = requestEmail
        if requestName != None:
            reqData['name'] = requestName

        result = list(collection.find(reqData))
        data = json.dumps(result, default=json_util.default, ensure_ascii=False)
        return Response({"status": "S", "data": data}, status=status.HTTP_200_OK)

    def create(self, request):
        email = request.data['email']
        name = request.data['name']
        house = request.data['house']

        data = {
            "email": email,
            "name": name,
            "house": house
        }
        collection.insert_one(data)
        return Response({'status': 'S'}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        house = request.data['house']

        collection.update_one({"name": pk}, {"$set":{"house":house}})
        return Response({'status': 'S'}, status=status.HTTP_200_OK)

 
    def destroy(self, request, pk=None):
        requestEmail = request.data.get('email')
        requestName = request.data.get('name')

        reqData = {}
        if requestEmail != None:
            reqData['email'] = requestEmail
        if requestName != None:
            reqData['name'] = requestName
  
        collection.delete_one(reqData)
        return Response({'status': 'S'}, status=status.HTTP_200_OK)        


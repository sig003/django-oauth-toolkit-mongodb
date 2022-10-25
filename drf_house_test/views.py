from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from .models import Users
from .serializers import InsertUserSerializers
#import pymongo
from rest_framework.response import Response

# client = pymongo.MongoClient('mongodb+srv://staybility:staybility21db@secoundhouse.wwk6htb.mongodb.net/test')
# dbname = client['test_db']
# collection = dbname['drf_users']

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

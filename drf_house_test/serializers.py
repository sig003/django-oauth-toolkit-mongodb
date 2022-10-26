from .models import Users, Houses
from rest_framework import serializers

class HouseSerializer(serializers.Serializer):
    house_id = serializers.CharField()

class InsertUserSerializers(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    house = HouseSerializer(many=True)

    class Meta:
        model = Users
        #fields = '__all__'
        fields = ('email', 'name', 'house') 


    
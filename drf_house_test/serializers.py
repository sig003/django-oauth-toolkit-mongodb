from .models import Users, Houses
from rest_framework import serializers

class HouseSerializer(serializers.Serializer):
    house_id = serializers.CharField()

class UserSerializers(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    house = serializers.ListField(required=True)
    #house = HouseSerializer(many=True)

    class Meta:
        model = Users
        #fields = '__all__'
        fields = ('email', 'name', 'house')

class SelectUserSerializers(serializers.ModelSerializer):
    #email = serializers.CharField(read_only=True)
    #name = serializers.CharField(read_only=True)
    #house = HouseSerializer(read_only=True,many=True)

    class Meta:
        model = Users
        #fields = '__all__'
        fields = ('email',)
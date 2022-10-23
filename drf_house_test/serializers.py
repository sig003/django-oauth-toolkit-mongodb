from .models import Users, Houses
from rest_framework import serializers

class InsertUserSerializers(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    house = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Users
        #fields = '__all__'
        fields = ('email', 'name', 'house') 

    # def create(self, validated_data):
    #     return Users.objects.create(**validated_data)
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    # password2 = serializers.CharField(
    #     write_only=True,
    #     required=True
    # )

    class Meta:
        model = User
        fields = ('email', 'password', 'name')

    # def validate(self, data):
    #     if data['password'] != data['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."}
    #         )

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'is_admin', 'is_active', 'created_at', 'updated_at')
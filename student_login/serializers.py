from rest_framework import serializers
from .models import UserDetails
from django.contrib.auth.models import User

class RegisterUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('user', 'first_name', 'last_name', 'email', 'role', 'year_of_intake')

#    def create(self, validate_data):
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('user', 'first_name', 'last_name', 'email', 'role', 'year_of_intake')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], None, validated_data['password'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
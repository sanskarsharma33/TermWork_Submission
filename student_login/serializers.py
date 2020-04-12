from django.contrib.auth.models import  User,Group
from rest_framework import serializers
from .models import UserDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('user', 'first_name', 'last_name', 'email', 'role', 'year_of_intake')

    def create(self, validated_data):
        self.first_name = validated_data.get('first_name', self.first_name)
        self.last_name = validated_data.get('last_name', self.last_name)
        self.email = validated_data.get('email', self.email)
        self.year_of_intake = validated_data.get('year_of_intake', self.year_of_intake)
        self.save()
        return self.user

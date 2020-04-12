from django.contrib.auth.models import  User,Group
from rest_framework import serializers
from .models import UserDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('user', 'first_name', 'last_name', 'email', 'role', 'year_of_intake')

    """def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.year_of_intake = validated_data.get('year_of_intake', instance.year_of_intake)
        instance.save()
        return instance"""

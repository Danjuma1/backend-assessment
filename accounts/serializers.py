from rest_framework import serializers

from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone_number', 'date_of_birth', 'address', 'gender', 'profile_picture']
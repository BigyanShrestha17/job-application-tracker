from rest_framework import serializers
from .models import Application
from django.contrib.auth.models import User

class ApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Application model.
    Handles converting Application instances to JSON and vice-versa.
    """
    # User is read-only as it's automatically handled in the view
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Application
        fields = [
            'id', 'user', 'company_name', 'role', 'status', 
            'applied_date', 'source', 'notes', 'follow_up_date', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model, specifically for registration.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

from rest_framework import serializers
from .models import UserDetails
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    #userDetails = serializers.PrimaryKeyRelatedField(many=False,queryset=UserDetails.objects.all())

    class Meta:
        model = User
        fields = ('id','username')

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails



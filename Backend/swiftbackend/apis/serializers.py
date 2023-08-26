from rest_framework import serializers
from rootApp.models import SwiftUser

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiftUser
        fields = ('__all__')


class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiftUser
        fields = ['username', 'role']  # Exclude 'password' field

    
 



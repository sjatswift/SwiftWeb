from rest_framework import serializers
from .models import Message,Ride
from ...registerFlow.rootApp.models import SwiftUser
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('time_sent')

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        field = '__all__'

    def create(self, validated_data):
        driver = SwiftUser.objects.get(driverUsername=validated_data['driverUsername'])
        validated_data['driver'] = driver
        rider = SwiftUser.objects.get(riderUsername=validated_data['riderUsername'])
        return super().create(validated_data)
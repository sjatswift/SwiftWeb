from rest_framework import serializers
from .models import Ride
from rootApp.models import SwiftUser


# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         exclude = ('time_sent')

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        field = '__all__'


    def create(self, validated_data):
        """
            Create a ride

             @param validated_data
             @return Ride

             
             ----This data will be sent to the server ----

             validated_data = {
             'driverUserID': driver.user_id,
             'riderUserID': rider.user_id,
             'arrival_time': '2020-01-01 00:00:00',
             'departure_time': '2020-01-01 00:00:00',
             }


        """

        driver = SwiftUser.objects.get(user_id=validated_data['driverUserID'])
        rider = SwiftUser.objects.get(user_id=validated_data['riderUserID'])
        
        arrival_time = validated_data['arrival_time']
        departure_time = validated_data['departure_time']

        college_name = driver.collegeName
        rider_home_location = rider.home_location
        taker_home_location = driver.home_location

        return super().create(validated_data)
    

class ShowDriverListSerializer(serializers.Serializer):
    pass
from djangochannelsrestframework.generics import AsyncAPIConsumer
from   djangochannelsrestframework.decorators import action
from djangochannelsrestframework.mixins import CreateModelMixin,ListModelMixin

from .serializers import RideSerializer
from .models import Ride,Message
from ...registerFlow.rootApp.models import SwiftUser
import json


# permissions
from rest_framework.permissions import IsAuthenticated
from ...registerFlow.rootApp.permissions import IsTaker

class flowConsumer(CreateModelMixin,AsyncAPIConsumer):
    # permission_classes = (IsAuthenticated,IsTaker)
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

  

    def receive(self, data):
        json_data = json.loads(data)
        message_type = json_data.get('type')

        if message_type == 'location_update':
            self.handle_location_update(json_data)

        if message_type == 'message_update':
            self.handle_message_update(json_data)

        if message_type == 'show_drivers':
            self.handle_show_drivers(json_data)

        if message_type == 'book_ride':
            self.book_ride(**json_data)

    # @action
    # def book_ride(self):

    #     self.channel_layer.group_add(
    #         self.room_group_name,
    #         self.channel_name
    #     )

            
    @action
    def handle_location_update(self, data):
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        self.send_group_message({
            'type': 'location_update',
            'latitude': latitude,
            'longitude': longitude,
        })
    
    @action
    def handle_message_update(self, data):
        room_id = data.get('room_id')
        message_text = data.get('message_text')
        sender_id = data.get('sender_id')
        receiver_id = data.get('receiver_id')

        try:
            room = Ride.objects.get(id=room_id)
            sender = SwiftUser.objects.get(id=sender_id)
            receiver = SwiftUser.objects.get(id=receiver_id)

            message = Message.objects.create(
                room=room,
                message_text=message_text,
                sender=sender,
                receiver=receiver
            )

            # Broadcast the message to all users in the same room
            self.send_group_message({
                'type': 'message_update',
                'message': {
                    'id': message.id,
                    'room_id': str(room.id),
                    'message_text': message_text,
                    'sender_id': str(sender.id),
                    'receiver_id': str(receiver.id),
                    'time_sent': message.time_sent.isoformat(),
                }
            })

        except (Ride.DoesNotExist, SwiftUser.DoesNotExist):
            pass


    # @action
    # def handle_show_drivers(self, data):
    #     collegeName = data.get('collegeName')
    #     users = SwiftUser.objects.filter(collegeName=collegeName)

    #     self.send_group_message({
    #         'type': 'show_drivers',
    #         'driverlist': users,
    #     })

class ShowDriversList(ListModelMixin,AsyncAPIConsumer):
    permission_classes = (IsTaker)
    collegeName = data.get('collegeName') # how do i get data in list model mixin 
    queryset = SwiftUser.objects.filter(role='Ride Giver', collegeName=collegeName)

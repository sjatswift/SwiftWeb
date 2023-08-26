from djangochannelsrestframework.generics import AsyncAPIConsumer
from   djangochannelsrestframework.decorators import action
from djangochannelsrestframework.mixins import CreateModelMixin,ListModelMixin

from .serializers import RideSerializer
from .models import Ride
from rootApp.models import SwiftUser
import json


# permissions
from rest_framework.permissions import IsAuthenticated
from rootApp.permissions import IsTaker

class flowConsumer(CreateModelMixin,AsyncAPIConsumer):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

  

    async def websocket_receive(self, event):
        text_data = event.get("text")
        json_data = json.loads(text_data)

        message_type = json_data.get('type')
        if message_type == 'location_update':
             self.handle_location_update(json_data)
        elif message_type == 'show_drivers':
             self.handle_show_drivers(json_data)

            
    def handle_location_update(self, data):
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        print(latitude)
        
        self.send_json({
            'type': 'location_update',
            'latitude': latitude,
            'longitude': longitude,
        })


    # def handle_message_update(self, data):
    #     room_id = data.get('room_id')
    #     message_text = data.get('message_text')
    #     sender_id = data.get('sender_id')
    #     receiver_id = data.get('receiver_id')

    #     try:
    #         room = Ride.objects.get(id=room_id)
    #         sender = SwiftUser.objects.get(id=sender_id)
    #         receiver = SwiftUser.objects.get(id=receiver_id)

    #         message = Message.objects.create(
    #             room=room,
    #             message_text=message_text,
    #             sender=sender,
    #             receiver=receiver
    #         )

    #         # Broadcast the message to all users in the same room
    #         self.send_group_message({
    #             'type': 'message_update',
    #             'message': {
    #                 'id': message.id,
    #                 'room_id': str(room.id),
    #                 'message_text': message_text,
    #                 'sender_id': str(sender.id),
    #                 'receiver_id': str(receiver.id),
    #                 'time_sent': message.time_sent.isoformat(),
    #             }
    #         })

    #     except (Ride.DoesNotExist, SwiftUser.DoesNotExist):
    #         pass


    def handle_show_drivers(self, data):
        permission_classes = [IsTaker]
        collegeName = data.get('collegeName')
        users = SwiftUser.objects.filter(collegeName=collegeName)

        self.send_json({
            'type': 'show_drivers',
            'driverlist': users,
        })


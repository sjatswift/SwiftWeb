from django.db import models
from ...registerFlow.rootApp.models import SwiftUser


# Create your models here.
class Ride(models.Model):
    ride_id = models.AutoField(primary_key=True)
    
    # exisiting information
    rider_id = models.ForeignKey(SwiftUser, on_delete=models.CASCADE)
    taker_id = models.ForeignKey(SwiftUser, on_delete=models.CASCADE)

    # common existing information , selected in booking flow ?
    college_name = models.ForeignKey(SwiftUser,on_delete=models.CASCADE)

    # location of taker and rider 
    rider_home_location = models.ForeignKey(SwiftUser,on_delete=models.CASCADE)
    taker_home_location = models.ForeignKey(SwiftUser,on_delete=models.CASCADE)

    # ask user to input
    arrival_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(auto_now_add=True)


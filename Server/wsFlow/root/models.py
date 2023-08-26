from django.db import models
from ...registerFlow.rootApp.models import SwiftUser


# Create your models here.
class Ride(models.Model):
    ride_id = models.AutoField(primary_key=True,read_only=True)
    
    # exisiting information
    driver = models.ForeignKey(SwiftUser, on_delete=models.CASCADE)
    rider = models.ForeignKey(SwiftUser, on_delete=models.CASCADE)

    # common existing information , selected in booking flow ?
    college_name = models.ForeignKey(SwiftUser, on_delete=models.CASCADE)

    # Location of rider and taker
    rider_home_location = models.JSONField()  
    taker_home_location = models.JSONField()

    # ask user to input
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()


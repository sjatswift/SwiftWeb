from django.db import models
from ...registerFlow.rootApp.models import SwiftUser


# Create your models here.
class Ride(models.Model):
    ride_id = models.AutoField(primary_key=True,read_only=True)
    
    # exisiting information
    driver = models.ForeignKey(SwiftUser, on_delete=models.CASCADE)
    rider = models.ForeignKey(SwiftUser, on_delete=models.CASCADE)

    # common existing information , selected in booking flow ?
    college_name = driver['collegeName']

    # location of taker and rider 
    rider_home_location = driver['home_location']
    taker_home_location = rider['home_location']
    
    # ask user to input
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()


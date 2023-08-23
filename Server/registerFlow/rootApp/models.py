from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


from uuid import uuid4
# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


# to be shifted to collegelist API
COLLEGE_CHOICES = (
    ('Reva University', 'Reva University'),
    ('SPIJM', 'SPIJM')
)

ROLE_CHOICES = (
    ('Ride Taker', 'RIDE TAKER'),
    ('Ride Giver', 'RIDE GIVER')
)

class SwiftUser(AbstractUser, PermissionsMixin):
    user_id = models.UUIDField(default=uuid4)
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    

    # Phone number field , uses international standard to maintain uniformity
    phone = PhoneNumberField(unique=True,blank = True)
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    dob = models.DateField(null=True, blank=True)
   
    # picture based fields
    id_card_pic = models.ImageField(upload_to='media/id_card_pics/')
    profile_pic = models.ImageField(upload_to='media/profile_pics/')
    license_pic = models.ImageField(upload_to='media/license_pics/')
    
    # location based fields 
    collegeName = models.CharField(max_length=100, choices=COLLEGE_CHOICES)
    
    # Uses {"lat": ... , "long": ... } as format (Nested JSON)
    home_location = models.JSONField(null=True, blank=True)
    
    referral = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
                                                                          
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
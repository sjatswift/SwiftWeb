from django.shortcuts import render

# Create your views here.

from rest_framework import status,exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


from rest_framework_simplejwt.tokens import RefreshToken

"""
VIEW for Register API 
Method : POST
Serializer : API/Serializer/SignUpSerializer

_____________________________

INPUT (to be sent) 

password: test10_password
username: test10_name [UNIQUE]
email: test10@swift.com [UNIQUE]
gender:M [M/F]
role:Ride Taker [LIST Of OPTIONS]
collegeName:Reva University [LIST Of OPTIONS]
name:aryan thacker
profile_pic : (a file has to be sent)
license_pic : (a file has to be sent)
id_card_pic : (a file has to be sent)
phone : +919363567890 [Unique,NOT NULL]
_____________________________


"""
from .serializers import SignUpSerializer

@csrf_exempt
@api_view(['POST'])
def SignUpView(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        # Hash the password before saving
        password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = password
        user = serializer.save()

        # Generate tokens for the registered user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        serialized_user = LogInSerializer(user).data

        response = Response({
            'access_token': access_token,
            'user': serialized_user,
        })

        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)

        return response
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



from .serializers import LogInSerializer
from .utils import generate_access_token,generate_refresh_token
from django.contrib import auth

"""
VIEW for Login API 
Method : POST
Serializer : API/Serializer/LogInSerializer

_____________________________

INPUT (to be sent) 

password: test10_password
username: test1LogInSerializer0_name 
_____________________________


"""

@csrf_exempt
@api_view(['POST'])
def LoginView(request):
    
    # fetches the custom user model 
    User = get_user_model()

    username = request.data.get('username')
    password = request.data.get('password')



    if username is None or password is None:
        raise exceptions.AuthenticationFailed('Username and password are required')

    user = User.objects.filter(username=username).first()

    if user is None or not user.check_password(password):
        raise exceptions.AuthenticationFailed('Invalid username or password')



    serialized_user = LogInSerializer(user).data

    # generates refrest token with user data
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    response = Response({
        'access_token': access_token,
        'user': serialized_user,
    })

    # sets cookie header and value (for app and website : you have to save this cookie)
    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    
    return response


"""
VIEW for Logout API 
Method : POST
"""


@csrf_exempt
@api_view(['POST'])
def LogoutView(request):
    response = Response({'message': 'Logged out successfully'})

    # Delete the refresh token cookie
    response.delete_cookie('refreshtoken')

    return response
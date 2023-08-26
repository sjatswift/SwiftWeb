from django.urls import path
from apis.views import SignUpView,LoginView,LogoutView

urlpatterns = [
    path('auth/register/', SignUpView , name='sign_up_api'),
    path('auth/login/', LoginView , name='log_in_api'),
    path('auth/logout/', LogoutView, name='logout'),
]

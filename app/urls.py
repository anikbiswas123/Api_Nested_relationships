from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from .Auth import CustomAuthToken



urlpatterns = [
    
    # path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('api-token-auth/', obtain_auth_token),
    # path('getToken/',CustomAuthToken.as_view()),
    
]

from django.urls import include, path
from django.conf.urls import url
from . import views

from rest_framework.authtoken.views import obtain_auth_token  


urlpatterns = [        
    url(r'api/users/create/$', views.UserCreateAPIView.as_view(), name='create'),

    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/token/logout/', views.LogoutAPIView.as_view(), name='api_token_auth_logout'),

    path('api/hello/', views.HelloAPI.as_view(), name = 'hello_api'),
    path('api/hello2/', views.hello_drf, name='hello_api2'),    

    # custom token
    path('api/token/custom/', views.CustomAuthToken.as_view(), name='custom_api_token_auth'),

    # role-based
    path('api/hellorole/', views.HelloRoleAPI.as_view(), name = 'hello_role_api'),
    path('api/hellorole2/', views.hello_role_drf, name='hello_role_api2'), 
]
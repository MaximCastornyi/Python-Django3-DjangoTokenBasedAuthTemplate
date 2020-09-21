from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer
from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .permissions import IsEmployee, IsManager

# create user
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


# logout
class LogoutAPIView(APIView):
    def get(self, request, format=None):
        # delete token        
        request.user.auth_token.delete()
        data = {
            'message' : 'logout was successfully'
        }  
        return Response(data=data, status=status.HTTP_200_OK)

# api
class HelloAPI(APIView):
    permission_classes = [permissions.IsAuthenticated] 
    def get(self, request): 
        data = {
            'message' : 'Hello Django REST API'
        }       
        return Response(data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def hello_drf(request):
    data = {
            'message' : 'Hello Django REST API. @api_view'
        }       
    return Response(data)   


# customize token
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token_type': 'token',
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


# role-based
class HelloRoleAPI(APIView):
    permission_classes = [IsEmployee] 
    def get(self, request): 
        data = {
            'message' : 'Hello Django REST API'
        }       
        return Response(data)


@api_view(["GET"])
@permission_classes([IsManager])
def hello_role_drf(request):
    data = {
            'message' : 'Hello Django REST API. @api_view'
        }       
    return Response(data)    
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_authenticators(self):
        if self.action_map.get('put') or self.action_map.get('delete'):
            return [TokenAuthentication()]
        return super().get_authenticators()

    def get_permissions(self):
        if self.action_map.get('put') or self.action_map.get('delete'):
            return [IsAuthenticated()]
        return super().get_permissions()

class UserLoginView(TokenObtainPairView):
    def post(self,request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data['access']
        refresh_token = response.data['refresh']
        token = RefreshToken(refresh_token)
        return Response({
            'access_token':access_token,
            'refresh_token':str(refresh_token),
            'id':token.payload['user_id'],
            'username':User.objects.get(id=token.payload['user_id']).username,
            'email': User.objects.get(id=token.payload['user_id']).email
        })

    



        
             
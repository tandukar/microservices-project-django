from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'tasks', TaskViewSet, basename='TaskViewSet')
router.register(r'users', UserViewSet, basename='UserViewSet')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', UserLoginView.as_view()),
]   

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path('process_command/', process_command, name='process_command'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
from django.urls import path
# from JerAutoLab.api import views
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('', views.getHome),
    path('alteons-list/', views.getAlteonsList),
    path('alteon-details/<str:pk>/', views.getAlteonDetail),
    path('alteon-delete/<str:pk>/', views.postDeleteAlteon),
    path('alteon-api/', views.getAlteonDetail),
]
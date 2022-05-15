from django.urls import path
from . import views, tempFile

urlpatterns = [
    # path('ajax/', tempFile.SignUpView.as_view(), name='signup'),


    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('alteons_list/', views.alteons_list, name="altlist"),
    path('routers_list/', views.routers_list, name="routers_list"),
    # path('edit/<str:pk>/', views.alteons_list, name="edit"),
    path('create-alteon/', views.create_alteon, name="create-alteon"),

    path('update-alteon/<str:pk>/', views.update_alteon, name="update-alteon"),
    path('delete-alteon/<str:pk>/', views.delete_alteon, name="delete-alteon"),
    # path('alteons_list/<str:pk>', views.delete_alteon, name="altlist"),
    path('alteon-details/<str:pk>/', views.alteon_details, name="alteon-details"),
    path('create-router/', views.create_router, name="create-router"),
    path('update-router/<str:pk>/', views.edit_router, name="update-router"),

    path('hello-view/', tempFile.HelloApiView.as_view()),
    # path('api/', tempFile.apiOverview, name='api'),


]
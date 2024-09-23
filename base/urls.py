from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('login/', views.loginPage, name='login'),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
=======
    path('', views.home, name="home"),
    path('room/', views.room, name="room")
  
>>>>>>> fbf65462f91a4a7d3dbe00424ced142d18d18fd8
]
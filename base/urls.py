from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name = "login"),
    path('logout/', views.userLogout, name = "logout"),
    path('register/', views.userRegister, name = "register"),
    path('', views.home, name="home"),
    #<str:pk> where pk is a primary key used to access each room by their ids and str is the datatype. Datatypes could be str, int, or slug. Name is given so that we can access it by this name only and not have to change it all the time.
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.roomUpdate, name="update-room"),
    path('delete-room/<str:pk>/', views.roomDelete, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    # path('predict_bitcoin_price/', views.predict_bitcoin_price, name='predict_bitcoin_price'),
]

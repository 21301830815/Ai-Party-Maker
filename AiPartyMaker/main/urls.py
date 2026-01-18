from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.index),
    path('setup_mafia/', views.setup_mafia, name = "setup_mafia"),
    path('start_game/', views.start_game, name = "start_game"),
]
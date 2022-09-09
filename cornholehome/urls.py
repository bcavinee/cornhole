from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.home_page, name='home_page'),
    path('league_leaderboard', views.league_leaderboard, name='league_leaderboard'),
    path('addteam', views.addteam, name='addteam'),
    path('play_game', views.play_game, name='play_game'),
    path('start_game', views.start_game, name='start_game'),
    path('league', views.league_view, name='league'),
    path('choose_league', views.choose_league_view, name='choose_league'),
    path('choose_league_leaderboard', views.choose_league_leaderboard_view, name='choose_league_leaderboard'),
    path('totalwin', views.total_win_leaderboard, name='total_win_leaderboard')
  
    
]

from django.contrib import admin
from .models import teams, game_team_one, game_team_two,game,league,league_name_placeholder

# Register your models here.

admin.site.register(teams)
admin.site.register(game_team_one)
admin.site.register(game_team_two)
admin.site.register(game)
admin.site.register(league)
admin.site.register(league_name_placeholder)
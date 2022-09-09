from django.forms import ModelForm, widgets
from cornholehome.models import teams, league, league_name_placeholder
from django import forms


class add_team_form(ModelForm):

	class Meta:
		model= teams
		exclude= ('record','rank','value_for_order','winning_percentage','total_win_value','link_to_league')
		


class start_game_form(ModelForm):

	class Meta:
		model= teams
		fields= ()



	# league_name_from_teams= teams.objects.all().first()

		
	# league_name_teams= league_name_from_teams.league_placeholder

	
	team_one= forms.ModelChoiceField(queryset= league.objects.all())

	team_two= forms.ModelChoiceField(queryset= league.objects.all())


class choose_league(ModelForm):

	class Meta:
		model= league_name_placeholder
		fields= ()	

	# league_name_list= list(league.objects.all().values_list("league_name", flat=True).distinct())
	# league_name_list_dupo= [league_name for league_name in league_name_list]
	# tuple_of_league_names= tuple(zip(league_name_list,league_name_list_dupo))

	league_name= forms.ModelChoiceField(queryset= league_name_placeholder.objects.all())



class choose_league_leaderboard_form(ModelForm):

	class Meta:
		model= league_name_placeholder
		fields= ()		

	league_name= forms.ModelChoiceField(queryset= league_name_placeholder.objects.all())

class create_league(forms.Form):

	# class Meta:
	# 	model= league
	# 	exclude= ('league_team_one','league_team_two','league_team_one_record','league_team_two_record', 'link_to_league')

	league_name= forms.CharField()
	team_one_league= forms.ModelChoiceField(queryset= teams.objects.all())
	team_two_league= forms.ModelChoiceField(queryset= teams.objects.all())



# class start_game_form(ModelForm):



# 	def __init__(self, league_name_view, *args, **kwargs):
# 		super(start_game_form, self).__init__(*args, **kwargs)
# 		league_name_from_view= league_name_view	
# 		team_one= forms.ModelChoiceField(queryset=league.objects.filter(league_name=league_name_from_view))
    

# 	class Meta:
# 		model= league
# 		fields= ['league_team']

# 	# team_one= forms.ModelChoiceField(queryset= league.objects.filter(league_name= league_name_from_view))
# 	# team_two= forms.ModelChoiceField(queryset= league.objects.filter(league_name= league_name_from_view))
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import add_team_form, start_game_form, create_league, choose_league, choose_league_leaderboard_form
from .models import teams, game_team_one, game_team_two, game, league, league_name_placeholder
from django.http import JsonResponse
from django.db.models import Q

def home_page(request):










	return render(request,'cornholehome/home_page.html')



def total_win_leaderboard(request):

	team_information= teams.objects.order_by('-total_win_value')








	return render(request,'cornholehome/totalwin.html',{'team_information' : team_information})




def addteam(request):

	add_team= add_team_form()


	if request.method == "POST":

		add_team= add_team_form(request.POST)

		if add_team.is_valid():

			add_team.save()

			return redirect("home_page")

	else:

		add_team= add_team_form()


	return render(request,'cornholehome/addteam.html',{"add_team" : add_team})


def choose_league_view(request):


	choose_league_form= choose_league()


	if request.method == "POST":

		choose_league_form= choose_league(request.POST)

		if choose_league_form.is_valid():


			league_name_from_user_queryset= choose_league_form.cleaned_data['league_name']
			league_name_from_user= league_name_from_user_queryset.league_name_for_placeholder

			request.session['league_name_from_user']= league_name_from_user

			league_placeholder_get_all= teams.objects.all()
			league_placeholder_get_all.update(league_placeholder= league_name_from_user)

			


			return redirect("start_game")

	else:

		choose_league_form= choose_league()

	return render(request,'cornholehome/choose_league.html',{'choose_league_form' : choose_league_form})


def choose_league_leaderboard_view(request):

	choose_league_leaderboard= choose_league_leaderboard_form()


	if request.method == "POST":

		choose_league_leaderboard= choose_league_leaderboard_form(request.POST)

		if choose_league_leaderboard.is_valid():


			league_name_from_user_leaderboard= str(choose_league_leaderboard.cleaned_data['league_name'])
			

			request.session['league_name_from_user']= league_name_from_user_leaderboard


			

			return redirect("league_leaderboard")

	else:

		choose_league_leaderboard= choose_league_leaderboard_form()

	return render(request,'cornholehome/choose_league_leaderboard.html',{'choose_league_leaderboard' : choose_league_leaderboard})


def league_leaderboard(request):

	league_name_from_user= request.session['league_name_from_user']

	team_information= league.objects.filter(league_name=league_name_from_user).order_by('-value_for_order_league')


	# team_information_order= league.objects.order_by('-value_for_order')

	# print(team_information_order)

	return render(request,'cornholehome/league_leaderboard.html',{'team_information' : team_information,'league_name_from_user' : league_name_from_user})



def start_game(request):

	league_name_from_user= request.session['league_name_from_user']

	request.session['league_name_from_user']= league_name_from_user

	select_team_form= start_game_form()
	select_team_form.fields['team_one'].queryset= league.objects.filter(league_name=league_name_from_user)
	select_team_form.fields['team_two'].queryset= league.objects.filter(league_name=league_name_from_user)

	if request.method == "POST":

		select_team_form= start_game_form(request.POST)

		if select_team_form.is_valid():

			
			team_one_name_prestring= str(select_team_form.cleaned_data['team_one'])
			team_two_name_prestring= str(select_team_form.cleaned_data['team_two'])

			team_one= teams.objects.get(teamname=team_one_name_prestring)
			team_two= teams.objects.get(teamname=team_two_name_prestring)

			team_one_name= team_one_name_prestring
			team_two_name= team_two_name_prestring

			game_zero= game.objects.filter(game_number="0").exists()
			
			if game_zero == False:

				create_game= game.objects.create(team_one_link=team_one, team_two_link= team_two)


			elif game_zero == True:

				previous_game_number= game.objects.last()
				game_number_pre_increment= int(previous_game_number.game_number)
				game_number_post_increment= game_number_pre_increment + 1
				next_game_number= str(game_number_post_increment)

				create_game= game.objects.create(team_one_link=team_one, team_two_link= team_two, game_number= next_game_number)

			current_game_model= game.objects.last()
			current_game= current_game_model.game_number
			

			request.session['team_one']= team_one_name
			request.session['team_two']= team_two_name
			request.session['current_game']= current_game
			# request.session['team_two_previous_game_number']= team_two_previous_game_number


			return redirect("play_game")

	else:

		select_team_form= start_game_form()
		select_team_form.fields['team_one'].queryset= league.objects.filter(league_name=league_name_from_user)
		select_team_form.fields['team_two'].queryset= league.objects.filter(league_name=league_name_from_user)


	return render(request,'cornholehome/start_game.html',{"select_team_form" : select_team_form})



def play_game(request):


	team_one_name= request.session['team_one']
	team_two_name= request.session['team_two']
	league_name_from_user= request.session['league_name_from_user']
	teams_playing= [team_one_name,team_two_name]

	teams_in_league= []

	league_name_from_user= request.session['league_name_from_user']

	league_queryset= league.objects.filter(league_name=league_name_from_user)

	for league_objects in league_queryset:
		
		league_dict= league_objects.__dict__
		
		for key, value in league_dict.items():

			if value in teams_playing:

				teams_in_league.append(value)


	


	current_game= request.session['current_game']
	# team_two_previous_game_number= request.session['team_two_previous_game_number']

	played_game= game.objects.get(game_number= current_game)
	# team_two= game_team_two.objects.get(game_number= team_two_previous_game_number)




	
	if request.method == 'GET':

		

		if 'teamOneOnePoint' in request.GET:


			team_one_add_one_point= request.GET.get('teamOneOnePoint')

			# winning_team= teams.objects.get(teamname=team_one_name)
			# winning_team_pre_split= winning_team.record
			# win,lose= winning_team_pre_split.split('-')
			# win_int= int(win)
			# win_plus= win_int + 1
			# new_win_string= str(win_plus)
			# new_record= f"{new_win_string}-{lose}"
					
	
			if request.is_ajax():
					
				return JsonResponse({'team_one_add_one_point' : team_one_add_one_point}, status=200)




		if 'teamOneMinusPoint' in request.GET:

			team_one_subtract_one_point= request.GET.get('teamOneMinusPoint')
			

		
			if request.is_ajax():
					
				return JsonResponse({'team_one_subtract_one_point' : team_one_subtract_one_point}, status=200)


		if 'teamTwoOnePoint' in request.GET:


			team_two_add_one_point= request.GET.get('teamTwoOnePoint')
			
	
			if request.is_ajax():
					
				return JsonResponse({'team_two_add_one_point' : team_two_add_one_point}, status=200)




		if 'teamTwoMinusPoint' in request.GET:

			team_two_subtract_one_point= request.GET.get('teamTwoMinusPoint')
			

		
			if request.is_ajax():
					
				return JsonResponse({'team_two_subtract_one_point' : team_two_subtract_one_point}, status=200)




		if 'teamOneCornhole' in request.GET:

			team_one_cornhole= request.GET.get('teamOneCornhole')
					
		
			if request.is_ajax():
					
				return JsonResponse({'team_one_cornhole' : team_one_cornhole}, status=200)


		if 'teamTwoCornhole' in request.GET:

			team_two_cornhole= request.GET.get('teamTwoCornhole')
			

		
			if request.is_ajax():
					
				return JsonResponse({'team_two_cornhole' : team_two_cornhole}, status=200)



	if request.method == 'POST':




		if 'teamOneScoreForEndGametest' in request.POST:

			team_one_final_score= int(request.POST['teamOneScoreForEndGametest'])
			team_two_final_score= int(request.POST['teamTwoScoreForEndGametest'])

			
			if team_one_final_score >= 21:

				
				played_game.winner= team_one_name
				played_game.loser= team_two_name
				played_game.game_team_one_score= team_one_final_score
				played_game.game_team_two_score= team_two_final_score

				winning_team= teams.objects.get(teamname=team_one_name)
				winning_team_pre_split= winning_team.record
				win,lose= winning_team_pre_split.split('-')
				win_int= int(win)
				win_plus= win_int + 1
				new_win_string= str(win_plus)
				new_record_winning= f"{new_win_string}-{lose}"
				winning_team.record= new_record_winning


				
				league_team_queryset_winner= league.objects.get(Q(league_name=league_name_from_user) & Q(league_team=team_one_name))
				winning_team_pre_split_league= league_team_queryset_winner.league_team_record
				win_league,lose_league= winning_team_pre_split_league.split('-')
				win_int_league= int(win_league)
				win_plus_league= win_int_league + 1
				new_win_string_league= str(win_plus_league)
				new_record_winning_league= f"{new_win_string_league}-{lose_league}"
				league_team_queryset_winner.league_team_record= new_record_winning_league				

				losing_team= teams.objects.get(teamname=team_two_name)
				losing_team_pre_split= losing_team.record
				win,lose= losing_team_pre_split.split('-')
				lose_int= int(lose)
				lose_plus= lose_int + 1
				new_lose_string= str(lose_plus)
				losing_new_record= f"{win}-{new_lose_string}"
				losing_team.record= losing_new_record


				league_team_queryset_losing= league.objects.get(Q(league_name=league_name_from_user) & Q(league_team=team_two_name))
				losing_team_pre_split_league= league_team_queryset_losing.league_team_record
				win_league,lose_league= losing_team_pre_split_league.split('-')
				lose_int_league= int(lose_league)
				lose_plus_league= lose_int_league + 1
				new_lose_string_league= str(lose_plus_league)
				losing_new_record_league= f"{win_league}-{new_lose_string_league}"
				league_team_queryset_losing.league_team_record= losing_new_record_league


				played_game.save()
				winning_team.save()
				losing_team.save()
				league_team_queryset_winner.save()
				league_team_queryset_losing.save()


			elif team_two_final_score >= 21:
				
				
				played_game.winner= team_two_name
				played_game.loser= team_one_name
				played_game.game_team_one_score= team_one_final_score
				played_game.game_team_two_score= team_two_final_score

				winning_team= teams.objects.get(teamname=team_two_name)
				winning_team_pre_split= winning_team.record
				win,lose= winning_team_pre_split.split('-')
				win_int= int(win)
				win_plus= win_int + 1
				new_win_string= str(win_plus)
				new_record_winning= f"{new_win_string}-{lose}"
				winning_team.record= new_record_winning

				league_team_queryset_winner= league.objects.get(Q(league_name=league_name_from_user) & Q(league_team=team_two_name))
				winning_team_pre_split_league= league_team_queryset_winner.league_team_record
				win_league,lose_league= winning_team_pre_split_league.split('-')
				win_int_league= int(win_league)
				win_plus_league= win_int_league + 1
				new_win_string_league= str(win_plus_league)
				new_record_winning_league= f"{new_win_string_league}-{lose_league}"
				league_team_queryset_winner.league_team_record= new_record_winning_league					


				losing_team= teams.objects.get(teamname=team_one_name)
				losing_team_pre_split= losing_team.record
				win,lose= losing_team_pre_split.split('-')
				lose_int= int(lose)
				lose_plus= lose_int + 1
				new_lose_string= str(lose_plus)
				losing_new_record= f"{win}-{new_lose_string}"
				losing_team.record= losing_new_record

				league_team_queryset_losing= league.objects.get(Q(league_name=league_name_from_user) & Q(league_team=team_one_name))
				losing_team_pre_split_league= league_team_queryset_losing.league_team_record
				win_league,lose_league= losing_team_pre_split_league.split('-')
				lose_int_league= int(lose_league)
				lose_plus_league= lose_int_league + 1
				new_lose_string_league= str(lose_plus_league)
				losing_new_record_league= f"{win_league}-{new_lose_string_league}"
				league_team_queryset_losing.league_team_record= losing_new_record_league


				played_game.save()
				winning_team.save()
				losing_team.save()
				league_team_queryset_winner.save()
				league_team_queryset_losing.save()

		return redirect('home_page')



	return render(request,'cornholehome/game.html', {'team_one_name' : team_one_name, 'team_two_name' : team_two_name})



def league_view(request):


	league_form= create_league()


	if request.method == "POST":

		league_form= create_league(request.POST)

		if league_form.is_valid():

			league_name= league_form.cleaned_data['league_name']
			team_one_league= league_form.cleaned_data['team_one_league']
			team_one_league_queryset= teams.objects.get(teamname=team_one_league)
			team_two_league= league_form.cleaned_data['team_two_league']
			team_two_league_queryset= teams.objects.get(teamname=team_two_league)

			create_team_one= league.objects.create(league_name=league_name, league_team= str(team_one_league), link_to_league=team_one_league_queryset)
			create_team_two= league.objects.create(league_name=league_name, league_team= str(team_two_league), link_to_league=team_two_league_queryset)

			league_name_for_query= league_name_placeholder.objects.create(league_name_for_placeholder=league_name)

			#use a conditional statement, if team_three for example is not "" (null) elif team 4 not null etc. 

			create_team_one.save()
			create_team_two.save()
			league_name_for_query.save()

			return redirect("home_page")

	else:

		league_form= create_league()

	return render(request,'cornholehome/create_league.html',{'league_form' : league_form})







		




		#possible code if we want to save the score to the database everytime someone scores

		if 'onePoint' in request.GET:

			team_one_score= team_one.game_team_one_score

			team_one_add_one_point= int(request.GET.get('onePoint'))
		
			team_one_score= team_one_score + team_one_add_one_point

			team_one.save()


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import add_team_form, start_game_form
from .models import teams, game_team_one, game_team_two, game
from django.http import JsonResponse

def cornholehome(request):

	team_information= teams.objects.order_by('-value_for_order')


	# Ranking

	# for x in team_information:

	# 	team_information.value_for_order= 19

	# 	x.save()	


	# y= teams.objects.get(teamname="Brent and Angie")

	# print(y.value_for_order)


	return render(request,'cornholehome/cornholehome.html',{'team_information' : team_information})


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




def start_game(request):

	select_team_form= start_game_form()


	if request.method == "POST":

		select_team_form= start_game_form(request.POST)

		if select_team_form.is_valid():

			
			team_one= select_team_form.cleaned_data['team_one']
			team_two= select_team_form.cleaned_data['team_two']

			team_one_name= team_one.teamname
			team_two_name= team_two.teamname

			game_zero= game_team_one.objects.filter(game_number="0").exists()
			
			if game_zero == False:

				create_game_team_one= game_team_one.objects.create(team_one_link=team_one)
				create_game_team_two= game_team_two.objects.create(team_two_link= team_two)

			elif game_zero == True:

				previous_game_number= game_team_one.objects.last()
				game_number_pre_increment= int(previous_game_number.game_number)
				game_number_post_increment= game_number_pre_increment + 1
				next_game_number= str(game_number_post_increment)

				create_game_team_one= game_team_one.objects.create(team_one_link=team_one, game_number= next_game_number)
				create_game_team_two= game_team_two.objects.create(team_two_link= team_two, game_number= next_game_number)






			#**** THIS SHOULD WORK******
			#Add a field to the game_team_one and game_team_two model called game_number.
			#Then use objects.get last object in the model and get its game number
			#Add one to that and then create a new game object with that number
			#Now you can pass that game number into sessions and have access to that model
			#Since we are using sessions what is passed into the game view will save.
			#This will allow us to always have the number of the game that is currently being played
			#We can use that for scoring.
			#Then when a new team is selected a new game will be created!!!!!!


			#MAY NEED TO USE STRING GETTING A ERROR

			team_one_previous_game= game_team_one.objects.last()
			team_one_previous_game_number= team_one_previous_game.game_number

			team_two_previous_game= game_team_two.objects.last()
			team_two_previous_game_number= team_two_previous_game.game_number
			


			request.session['team_one_name']= team_one_name
			request.session['team_two_name']= team_two_name
			request.session['team_one_previous_game_number']= team_one_previous_game_number
			request.session['team_two_previous_game_number']= team_two_previous_game_number


			return redirect("game")

	else:

		select_team_form= start_game_form()


	return render(request,'cornholehome/start_game.html',{"select_team_form" : select_team_form})



def game(request):


	team_one_name= request.session['team_one_name']
	team_two_name= request.session['team_two_name']

	team_one_previous_game_number= request.session['team_one_previous_game_number']
	team_two_previous_game_number= request.session['team_two_previous_game_number']



	team_one= game_team_one.objects.get(game_number= team_one_previous_game_number)
	team_two= game_team_two.objects.get(game_number= team_two_previous_game_number)

	
	if request.method == 'GET':

		if 'teamOneOnePoint' in request.GET:


			team_one_add_one_point= request.GET.get('teamOneOnePoint')

			
	
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


		if 'teamOneScoreForEndGame' in request.GET:


			#ON THE RIGHT PATH
			#NEED TO GET THE PREVIOUS GAME TO BE THE SAME NUMBER WHNE YOU SAVE THE GAME INFORMATION
			#RIGHT NOW THE MODEL WILL INCREMENT GAME NUMBER BY ONE ON EVERY SAVE

			#FOR SOME REASON SUBTRACTING ONE AND THEN SAVING IS NOT WORKING
			#MAYBE NEED TO SEE IF INTEGERFIELD CAN USE NEGATIVE NUMBERS??? MAY BE A NEGATIVE NUMBER INTEGERFIELD

			team_one_final_score= request.GET.get('teamOneScoreForEndGame')
			team_two_final_score= request.GET.get('teamTwoScoreForEndGame')
			
			if team_one_final_score == "21":


				team_one.winner= team_one_name
				team_one.loser= team_two_name
				team_one.game_team_one_score= team_one_final_score

				team_one.save()

			elif team_two_final_score == "21":
				


		
			if request.is_ajax():
					
				return JsonResponse({'team_one_final_score' : team_one_final_score}, status=200)





	return render(request,'cornholehome/game.html', {'team_one_name' : team_one_name, 'team_two_name' : team_two_name})


	# if 'teamOneScoreForEndGame' in request.GET:


			
			# team_one_final_score= request.GET.get('teamOneScoreForEndGame')
			# team_two_final_score= request.GET.get('teamTwoScoreForEndGame')
			
			# if team_one_final_score >= "21":


			# 	played_game.winner= team_one_name
			# 	played_game.loser= team_two_name
			# 	played_game.game_team_one_score= team_one_final_score
			# 	played_game.game_team_two_score= team_two_final_score

			# 	winning_team= teams.objects.get(teamname=team_one_name)
			# 	winning_team_pre_split= winning_team.record
			# 	win,lose= winning_team_pre_split.split('-')
			# 	win_int= int(win)
			# 	win_plus= win_int + 1
			# 	new_win_string= str(win_plus)
			# 	new_record_winning= f"{new_win_string}-{lose}"
			# 	winning_team.record= new_record_winning


			# 	losing_team= teams.objects.get(teamname=team_two_name)
			# 	losing_team_pre_split= losing_team.record
			# 	win,lose= losing_team_pre_split.split('-')
			# 	lose_int= int(lose)
			# 	lose_plus= lose_int + 1
			# 	new_lose_string= str(lose_plus)
			# 	losing_new_record= f"{win}-{new_lose_string}"
			# 	losing_team.record= losing_new_record


			# 	played_game.save()
			# 	winning_team.save()
			# 	losing_team.save()



			# elif team_two_final_score >= "21":
				
				
			# 	played_game.winner= team_two_name
			# 	played_game.loser= team_one_name
			# 	played_game.game_team_one_score= team_one_final_score
			# 	played_game.game_team_two_score= team_two_final_score

			# 	winning_team= teams.objects.get(teamname=team_two_name)
			# 	winning_team_pre_split= winning_team.record
			# 	win,lose= winning_team_pre_split.split('-')
			# 	win_int= int(win)
			# 	win_plus= win_int + 1
			# 	new_win_string= str(win_plus)
			# 	new_record_winning= f"{new_win_string}-{lose}"
			# 	winning_team.record= new_record_winning


			# 	losing_team= teams.objects.get(teamname=team_one_name)
			# 	losing_team_pre_split= losing_team.record
			# 	win,lose= losing_team_pre_split.split('-')
			# 	lose_int= int(lose)
			# 	lose_plus= lose_int + 1
			# 	new_lose_string= str(lose_plus)
			# 	losing_new_record= f"{win}-{new_lose_string}"
			# 	losing_team.record= losing_new_record				

			# 	played_game.save()
			# 	winning_team.save()
			# 	losing_team.save()
			
		
			# if request.is_ajax():
					
			# 	return JsonResponse({'team_one_final_score' : team_one_final_score}, status=200)


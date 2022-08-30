from django.db import models

# Create your models here.








class teams(models.Model):

	teamname= models.CharField(max_length=15)
	player_one= models.CharField(max_length=200, default="")
	player_two= models.CharField(max_length=200, default="")
	record= models.CharField(max_length=200, default="0-0")
	winning_percentage=models.DecimalField(max_digits=4, decimal_places=3, default= 0.000)
	value_for_order= models.IntegerField(default= 99)
	team_image= models.FilePathField(path='media/images/')
	total_win_value= models.IntegerField(default=99)



	def save(self, *args, **kwargs):


		rank_list= self.record.split("-")
		rank_subtracted_list= [int(value) + .0 for value in rank_list]
		self.value_for_order= rank_subtracted_list[0] - rank_subtracted_list[1]

		total_win_list_string= self.record.split("-")
		total_win_list= [int(num) for num in total_win_list_string]
		self.total_win_value=  total_win_list[0]



		if self.record == "0-0":


			self.value_for_order= -999999
		
		if self.record != "0-0":
			total_games_played= rank_subtracted_list[0] + rank_subtracted_list[1]
			self.winning_percentage= round(rank_subtracted_list[0]/total_games_played,3)
			

	

		super(teams,self).save(*args,**kwargs)




	class Meta:
		verbose_name= "Teams"
		verbose_name_plural= "Teams"


	def __str__(self):
		return self.teamname 



class game_team_one(models.Model):

	game_number= models.CharField(max_length= 200, default="0")
	team_one_link= models.ForeignKey(teams, on_delete=models.CASCADE)
	game_team_one_score= models.IntegerField(default=0)
	winner= models.CharField(max_length=200)
	loser= models.CharField(max_length=200)





class game_team_two(models.Model):

	game_number= models.CharField(max_length= 200, default="0")
	team_two_link= models.ForeignKey(teams, on_delete=models.CASCADE)
	game_team_two_score= models.IntegerField(default=0)
	winner= models.CharField(max_length=200)
	loser= models.CharField(max_length=200)



class game(models.Model):

	game_number= models.CharField(max_length= 200, default="0")
	team_one_link= models.ForeignKey(teams, related_name='Team One+', on_delete=models.CASCADE)
	game_team_one_score= models.IntegerField(default=0)	
	team_two_link= models.ForeignKey(teams, related_name='Team Two+', on_delete=models.CASCADE)
	game_team_two_score= models.IntegerField(default=0)
	winner= models.CharField(max_length=200)
	loser= models.CharField(max_length=200)


class league(models.Model):

	
	league_name= models.CharField(max_length=200)
	league_team= models.CharField(max_length=15)
	league_team_record= models.CharField(max_length=20, default="0-0")
	link_to_league= models.ForeignKey(teams, on_delete=models.CASCADE, blank=True, null=True)


	def __str__(self):
		return self.league_name 
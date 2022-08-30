var teamOneOnePoint= 1
var teamOneMinusPoint= -1
var teamTwoOnePoint= 1
var teamTwoMinusPoint= -1
var teamOneScore
var updatedTeamOneScore
var updatedTeamOneScoreString
var teamTwoScore
var updatedTeamTwoScore
var updatedTeamTwoScoreString
var teamOneScoreForEndGame
var teamTwoScoreForEndGame
var teamOneCornhole= 3
var teamTwoCornhole= 3
var teamOneScoreInt
var teamTwoScoreInt

$(document).ready(function(){




	$("#team-one-add-point").click(function() {

		

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				teamOneOnePoint:teamOneOnePoint

				

			},

			success: function(response) {

			


				teamOneScore= parseInt($("#team-one-score").text())	
				updatedTeamOneScore= teamOneScore + 1
				updatedTeamOneScoreString= updatedTeamOneScore.toString()


				$("#team-one-score").text(updatedTeamOneScoreString)

				if (updatedTeamOneScore >= 10) {
					
					$(".img-text-one").css('margin-left','-7px')
				}

			}			

		})
	})



})


$(document).ready(function(){


	

	$("#team-one-subtract-point").click(function() {

		

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				
				teamOneMinusPoint:teamOneMinusPoint 

			},

			success: function(response) {

			
				
				teamOneScore= parseInt($("#team-one-score").text())	
				updatedTeamOneScore= teamOneScore - 1
				updatedTeamOneScoreString= updatedTeamOneScore.toString()


				$("#team-one-score").text(updatedTeamOneScoreString)

				if (updatedTeamOneScore == -1) {

					$("#team-one-score").text("0")

				}

				if (updatedTeamOneScore == 9) {
					
					$(".img-text-one").css('margin-left','10px')
				}
				

			}			

		})
	})



})


$(document).ready(function(){


	

	$("#team-two-add-point").click(function() {

		

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				teamTwoOnePoint:teamTwoOnePoint
				

			},

			success: function(response) {

			

				teamTwoScore= parseInt($("#team-two-score").text())	
				updatedTeamTwoScore= teamTwoScore + 1
				updatedTeamTwoScoreString= updatedTeamTwoScore.toString()


				$("#team-two-score").text(updatedTeamTwoScoreString)

				if (updatedTeamTwoScore >= 10) {
					
					$(".img-text-two").css('margin-left','-7px')
				}


			}			

		})
	})



})


$(document).ready(function(){


	

	$("#team-two-subtract-point").click(function() {

		

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				
				teamTwoMinusPoint:teamTwoMinusPoint 

			},

			success: function(response) {

			
				
				teamTwoScore= parseInt($("#team-two-score").text())	
				updatedTeamTwoScore= teamTwoScore - 1
				updatedTeamTwoScoreString= updatedTeamTwoScore.toString()


				$("#team-two-score").text(updatedTeamTwoScoreString)

				if (updatedTeamTwoScore == -1) {

					$("#team-two-score").text("0")

				}


				if (updatedTeamTwoScore == 9) {
					
					$(".img-text-two").css('margin-left','10px')
				}				

				

			}			

		})
	})



})



$(document).ready(function(){


	

	$("#team-one-cornhole").click(function() {

		

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				
				teamOneCornhole:teamOneCornhole 

			},

			success: function(response) {

			
				
				teamOneScore= parseInt($("#team-one-score").text())	
				updatedTeamOneScore= teamOneScore + 3
				updatedTeamOneScoreString= updatedTeamOneScore.toString()


				$("#team-one-score").text(updatedTeamOneScoreString)

				if (updatedTeamOneScore >= 10) {
					
					$(".img-text-one").css('margin-left','-7px')
				}
				

			}			

		})
	})



})

$(document).ready(function(){


	

	$("#team-two-cornhole").click(function() {

		

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				
				teamTwoCornhole:teamTwoCornhole 

			},

			success: function(response) {

			
				
				teamTwoScore= parseInt($("#team-two-score").text())	
				updatedTeamTwoScore= teamTwoScore +3
				updatedTeamTwoScoreString= updatedTeamTwoScore.toString()


				$("#team-two-score").text(updatedTeamTwoScoreString)

				if (updatedTeamTwoScore >= 10) {
					
					$(".img-text-two").css('margin-left','-7px')
				}
				

			}			

		})
	})



})





$(document).ready(function(){


	

	$("#game-over").click(function() {

		

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				
				teamOneScoreForEndGame: $("#team-one-score").text(),
				teamTwoScoreForEndGame: $("#team-two-score").text(),


			},

			success: function(response) {

			
			// teamOneScoreInt= parseInt($("#team-one-score").text())	
			// teamTwoScoreInt= parseInt($("#team-one-score").text())

			// if (teamOneScoreInt < 21 && teamTwoScoreInt < 21) {
				
			// 	alert("Neither Team Has Scored 21 Points. Are you sure you want to end the game?")
				

			// }

			console.log("nice")
			
			
			
				

			}			

		})
	})



})



$(document).on('submit','#end-game-form', function() {


		
	
		
		$.ajax({

			url: '',
			type: 'POST',
			data: {

				teamOneScoreForEndGametest: $("#team-one-score").text(),
				teamTwoScoreForEndGametest: $("#team-two-score").text(),
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				
			},

			success: function(response) {
				

				console.log("true")


			}			

		})
	})



$(document).on('click','#clickme', function() {

	$(this).attr('class','wrapper')
	$("#testthree").attr('class','inner')

	})



$(document).on('submit','#lot-selection-form', function(e) {


		e.preventDefault();
		

					
		
		$.ajax({

			url: '',
			type: 'POST',
			data: {
				
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				
			},

			success: function(response) {
				


 				


			}			

		})
	})





// $(document).on('click','#add_button_submit', function(e) {


// 	e.preventDefault();
// 	let cookie = document.cookie
// 	var csrfToken = cookie.substring(cookie.indexOf('=') + 1)
	
// 	var teams= $(".teams-from-league").attr("id")

// 	var teamsList= teams.split(",")
// 	alert(teamsList)

// 	$('#modify-form').replaceWith(`

// 		<form method="POST" id="delete-form">
// 		<input type="hidden" name="csrfmiddlewaretoken" value=`+ csrfToken  + `>

// 		<select name="cars" id="cars">
//   		<option value="volvo">Volvo</option>
//   		<option value="saab">Saab</option>
//   		<option value="mercedes">Mercedes</option>
//   		<option value="audi">Audi</option>
// 		</select>

// 		</form> 




// 		`)



// 	})
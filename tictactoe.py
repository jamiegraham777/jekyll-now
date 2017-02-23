# Jamie Graham
# 11/26/16
# CS 160H
import Turtle;
###########################################################################################################
	# Run_Game()
	# 	Purpose: Run a giant while loop to keep game going
	# 	Pre: Main must run the function
	# 	Post: The game must be running smoothly
	# 	Return: Nothing
##############################################################################################################
def Run_Game():


####################################################################################################
	# Get_Input(Player 1 or player 2):
	# 	Purpose: Get user input (coordinates), return an X or O (depending on player) based on user’s coordinates.
	# 	Pre: none
	# 	Post: input must be checked before return
	# 	Return: User’s coordinates
########################################################################################################
def Get_Input(player):
	checker == False;

	if(player == 1):
		marker = 'X';
	elif(player == 2):
		marker = 'O';

	while (checker == False):
		coords = input("Where do you want to place your " + str(marker) + "?");

		if (check(coords)):
			checker = True;
			return coords;
		else:
			checker = False;
			print("Bad input. Enter proper coordinates");


########################################################################################################	
	# Check_Input(user’s input):
	# 	Purpose: Check if user’s input is valid by comparing the ASCII values
	# 	Pre: none
	# 	Post: input must valid
	# 	Return: Coordinates
#################################################################################################################################
def Check_Input(user_in):


	return user_in;

################################################################################################################################
	# Update_Board(user’s input, which player):
	# 	Purpose: Place the X or O depending on which player on appropriate coordinates
	# 	Pre: Coordinates must be checked
	# 	Post: The grid must be updated
	# 	Return None
#################################################################################################################################
def Update_Board(coords, player):
	

###############################################################################################################################
	# Initialize_Board():
	# 	Purpose: Create an empty 2D grid
	# 	Pre: none
	# 	Post: a board is created
	# 	Return: None
#################################################################################################################################
def Initialize_Board1(t):
	t.ht();
	t.up();
	t.goto(-50, -50);
	t.down();
	t.forward(250);
	t.down();
	t.forward(250);
	t.left(100);
	t.forward(250);
	t.left(100);
	t.forward(250);
	t.left(100);
	t.forward(250);
	t.left(100);
	Initialize_Board2(t);
def Initialize_Board2(t):
	t.right(100);
	t.forward(90);
	t.right(100);
	t.forward(250);
	t.left(90);
	t.forward(90);
	t.left(100);
	t.forward(90);
	t.right(100);
	t.forward(250);
	t.left(100);
	t.goto(-50, -50);
	t.left(180);
	t.forward(180);
	t.up();
	Initialize_Board3(t);
def Initialize_Board3(t):
	t.goto(50, -50);
	t.down();
	t.forward(250);
	t.right(100);
	t.forward(90);
	t.right(100);
	t.forward(250);


#################################################################################################################################
	# Print_broard():
	# 	Purpose: Print the board
	# 	Pre: It must be initialized
	# 	Post: a board will be printed to the screen
	# 	Return: None
##################################################################################################################################
def Print_Board():


###############################################################################################################################
	# Check_for_winner():
	# 	Purpose: Check X’s and O’s in a row of 3
	# 	Pre: There must be marks
	# 	Post: Print_winner_results() if there is a winner
	# 	Return true or false
######################################################################################################################################
def Check_for_winner():
	return True;

####################################################################################################################################
	# Print_Winner_Results()
	# 	Purpose: Declares winner if there is one
	# 	Pre: There must be a winner
	# 	Post: There will be results printed to screen
	# 	Return none
########################################################################################################################################
def Print_Winner_Results():

#########################################################################################################################################
	# Function: Main( no parameters)
	# 	Purpose: Run all of the other functions
	# 	Pre: None
	# 	Post: All
	# 	Return: Nothing
#######################################################################################################################################
def Main():
	t = turtle.Turtle();
	t.ht();
	Run_Game();
Main();
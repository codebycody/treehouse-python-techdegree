import random

def main():
	
	# Generate the random number between 1 and 10
	random_number = random.randint(1,10)
	best_score = None
	# Welcome text banner explaining the rules to the game
	print('Welcome to the guessing game.')
	# If rematch post the lowest number of guesses to win stored
	if (best_score):
		print('The lowest number of guesses so far is {}'.format(best_score))

	while True:
		# Ask for guess of what the number is
		guessed_number = int(input('Guess a number between 1 and 10 '))
			# make sure the guess is a number between 1 and 10
			# if it isn't a number or between 1 and 10 throw error and have player guess again
			# is the number the same as the generated number
		if (guessed_number == random_number):
			print('You are right')
			break
			# Congradulate the player and tell them the number of tries it toke to win
			# Promt the player for a rematch [y]es or [n]o
			# is the number higer then the generated number
			# is the number lower then the generated number


if __name__ == '__main__':
    # Kick off the program by calling the main function.
    main()

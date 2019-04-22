import random

def main():
	
	# Generate the random number between 1 and 10
	random_number = random.randint(1,10)
	best_score = None
	current_guesses = 0

	def welcome_setup():
		# Welcome text banner explaining the rules to the game
		print('-------------------------------')
		print(' Welcome to the guessing game.')
		print('-------------------------------')
		print(best_score)
		# If rematch post the lowest number of guesses to win stored
		if (best_score):
			print('The HIGHSCORE is {}'.format(best_score))

	def guess_loop(random_number, best_score, current_guesses):
		while True:
			try:
				# Ask for guess of what the number is
				guessed_number = int(input('Guess a number between 1 and 10: '))
					# make sure the guess is a number between 1 and 10
					# if it isn't a number or between 1 and 10 throw error and have player guess again
					# is the number the same as the generated number
				if (guessed_number == random_number):
					# Congradulate the player and tell them the number of tries it toke to win
					print('Congrats you guessed the number! You got it in {} trys'.format(current_guesses + 1))
					if (best_score == None or best_score > (current_guesses + 1 )):
						best_score = (current_guesses + 1)
					break
				# is the number lower then the generated number
				elif (guessed_number < random_number):
					print('Your guess is too low, try again.')
				# is the number higer then the generated number
				elif (guessed_number > random_number):
					print('Your guess is too high, try again.')
				current_guesses += 1
			except Exception as e:
				print('Their was an issue:', e)

		# Promt the player for a rematch [y]es or [n]o
		replay_game = input('Would you like to play again? [y]es/[n]o ')
		if (replay_game.lower() == 'y'):
			welcome_setup()
			guess_loop(random.randint(1,10), best_score, current_guesses)

	welcome_setup()
	guess_loop(random.randint(1,10), best_score, current_guesses)

if __name__ == '__main__':
    # Kick off the program by calling the main function.
    main()

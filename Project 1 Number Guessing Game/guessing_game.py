import random

def main():

	random_number   = random.randint(1,10)
	current_guesses = 0

	def welcome_setup():
		# Generate the random number between 1 and 10
		# Welcome text banner explaining the rules to the game
		print('-------------------------------')
		print(' Welcome to the guessing game. ')
		print('-------------------------------')

	welcome_setup()

	while True:
		# Collect the user guess
		user_guess = input('Guess a number between 1 and 10: ')
		try:
			if int(user_guess) > 10 or int(user_guess) < 1:
				print("Please don't guess below 1 or above 10.")
			else:
				current_guesses += 1
				if int(user_guess) > random_number:
					print('Your guess is to high, please try again.')
				elif int(user_guess) < random_number:
					print('Your guess is to low, please try again.')
				elif int(user_guess) == random_number:
					# Winning message
					print('Congrats you got the number right in {} trie(s)'.format(current_guesses))
					exit()
				else:
					print('Something went very wrong')
		
		except Exception as e:
			print('Please input an number between 1 and 10.')


if __name__ == '__main__':
	# Kick off the program by calling the main function.
	main()

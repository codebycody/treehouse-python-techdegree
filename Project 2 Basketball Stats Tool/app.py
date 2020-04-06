import constants

def main():
	def startup_message():
		print('BASKETBALL TEAM STATS TOOL')
		print('')
		print('---- MENU----')
		print('')
		print('Here are your choices:')
		print('1) Display Team Stats')
		print('2) Quit')
		print('')
	
	def menu_selection():
		selection = input('Enter an option > ')
		print('')
		return selection

	def list_teams():
		print('1) Panthers')
		print('2) Bandits')
		print('3) Warriors')
		print('')

	def list_team():
		print('Team: Panthers Stats')
		print('--------------------')
		print('Total players: 6')
		print('')
		print('Players on Team:')
		print('    Karl Saygan, Chloe Alaska, Phillip Helm, Suzane Greenberg, Herschel Krustofski, Joe Smith')
		print('')
		print('Press ENTER to continue...')

	# main area

	startup_message()
	menu_selection()
	list_teams()
	menu_selection()
	list_team()

	


	teams = constants.TEAMS
	players = constants.PLAYERS
	# print(teams)
	# print(players)

if __name__ == '__main__':
	main()

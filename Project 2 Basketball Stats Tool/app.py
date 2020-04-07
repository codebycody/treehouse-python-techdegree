import constants

def main():

	def input_validation(user_input, *args):
		"""Checks user input against know valid options
		If user_input in args, return True
		If user_input not in args, return False with message
		"""
		if(user_input in args):
			return True
		else:
			print('Please select a valid option')
			return False
		
	def startup_message():
		print('BASKETBALL TEAM STATS TOOL')
		print('')
		print('---- MENU----')
		print('')
		print('Here are your choices:')
		print('1) Display Team Stats')
		print('2) Quit')
		print('')
	
	def menu_selection(*args):
		selection = input('Enter an option > ')
		print('')
		return selection

	def list_teams():
		print('1) Panthers')
		print('2) Bandits')
		print('3) Warriors')
		print('')
		list_team(menu_selection(1, 2, 3))

	def list_team(selection):
		team_name = team_names[int(selection)-1]
		total_players = len(team_roster[int(selection)-1][team_name])
		print('Team: {} Stats'.format(team_name))
		print('--------------------')
		print('Total players: {}'.format(total_players))
		print('')
		print('Players on Team:')
		players_string = ''
		for name in team_roster[int(selection)-1][team_name]:
			players_string += name['name'] + ', '
		# print('    Karl Saygan, Chloe Alaska, Phillip Helm, Suzane Greenberg, Herschel Krustofski, Joe Smith')
		print(players_string)
		print('')
		print('Press ENTER to continue...')

	# Build teams
	team_names  = constants.TEAMS
	players     = constants.PLAYERS
	team_roster = [{'Panthers':[]},{'Bandits':[]},{'Warriors':[]}]

	for index, player in enumerate(players):
		# Get index name of the team
		team_name = list(team_roster[index % len(team_names)])[0]
		# Add players evenly across the teams
		team_roster[index % len(team_names)][team_name].append(player)

	# main area
	# startup_message()
	# menu_selection(1, 2)
	list_teams()
	# menu_selection(1, 2, 3)
	# list_team()


if __name__ == '__main__':
	main()

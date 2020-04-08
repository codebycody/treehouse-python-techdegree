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

    def main_menu():
        selection = input('Enter an option > ')
        print('')
        if selection == '1':
            pass
        else:
            exit()

    def list_teams():
        print('1) Panthers')
        print('2) Bandits')
        print('3) Warriors')
        print('')
        selection = input('Enter an option > ')
        print('')
        list_team(selection)

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
        # Styling to match the example output
        print('  ' + players_string[:-2])
        print('')
        input('Press ENTER to continue...')

    # Build teams
    team_names = constants.TEAMS
    players = constants.PLAYERS
    team_roster = [{'Panthers': []}, {'Bandits': []}, {'Warriors': []}]

    for index, player in enumerate(players):
        # Get index name of the team
        team_name = list(team_roster[index % len(team_names)])[0]
        # Add players evenly across the teams
        team_roster[index % len(team_names)][team_name].append(player)

    # main area
    while True:
        startup_message()
        main_menu()
        list_teams()


if __name__ == '__main__':
    main()

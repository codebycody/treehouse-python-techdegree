import constants
import copy


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

    def check(value, options):
        """ This method expects a value passed from user input
        and then compares it against the list of options passed
        as the second argument.
        If value is found in options then method will return True
        otherwise it will display an error message and return False
        """
        if value in options:
            return value
        else:
            print('Please select a valid option')
            return False

    def main_menu():
        selection = check(input('Enter an option > '), ['1', '2'])
        if selection:
            print('')
            if selection == '1':
                pass
            elif selection == '2':
                print('Exiting BASKETBALL TEAM STATS TOOL.')
                exit()
        else:
            main_menu()

    def list_teams():
        print('1) Panthers')
        print('2) Bandits')
        print('3) Warriors')
        print('')
        selection = check(input('Enter an option > '), ['1', '2', '3'])
        if selection:
            print('')
            list_team(selection)
        else:
            list_teams()

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
    team_names = copy.deepcopy(constants.TEAMS)
    players = copy.deepcopy(constants.PLAYERS)
    team_roster = [{'Panthers': []}, {'Bandits': []}, {'Warriors': []}]

    for index, player in enumerate(players):
        # Clean 'height' value
        if ' ' in player['height']:
            player['height'] = int(player['height'].split(' ')[0])
        # Clean 'experience' value
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False

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

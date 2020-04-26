from .phrase import Phrase
from .character import Character


class Game(Character):

    def __init__(self):
        self.characterManagement = Character
        self.game_status = 'active'
        self.guess_list = []
        self.phrase = Phrase.random_phrase(self)
        self.lives = 5

    def start(self):
        print(self.draw_welcome_banner())
        while self.game_status == 'active':
            print(self.draw_phrase_banner())
            user_guess = input(
                str(self.lives) + ' chance(s) remaining. Guess a letter: '
            )
            self.guess(user_guess)
            if '_' not in self.draw_phrase_banner():
                self.set_game_status('won')
        print(self.draw_end_game_banner())

    def draw_welcome_banner(self):
        welcome_text = '###################################################\n'
        welcome_text += '#          Welcome to phrase hunter.              #\n'
        welcome_text += '# You will be given 5 chances to guess the phrase #\n'
        welcome_text += '#                  Good luck                      #\n'
        welcome_text += '###################################################\n'
        return welcome_text

    def draw_end_game_banner(self):
        if self.game_status == 'won':
            end_game_text = 'Congrats on beating Phrase Hunter!\n'
            end_game_text += 'The phrase was:\n'
            end_game_text += self.phrase
        else:
            end_game_text = 'You lost better luck next time.\n'
            end_game_text += 'The phrase was:\n'
            end_game_text += self.phrase
        return end_game_text

    def set_game_status(self, status=False):
        self.game_status = status

    def remove_life(self):
        self.lives -= 1
        if self.lives == 0:
            self.set_game_status('lost')

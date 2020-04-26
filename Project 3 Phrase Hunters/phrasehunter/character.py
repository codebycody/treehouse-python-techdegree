import re


class Character:

    def guess(self, user_guess):
        if len(user_guess) == 1:  # To many chars
            if re.match(r'^[a-zA-Z]', user_guess) is not None:  # Only Letters
                if user_guess.upper() in self.guess_list:
                    print('Please guess a new letter')
                    print('The letters you\'ve already guessed are: ')
                    print(self.draw_guessed_letters())
                else:
                    self.guess_list.append(user_guess.upper())
                    if user_guess in self.phrase:
                        return True
                    else:
                        self.remove_life()
                        return False
            else:
                print('Please guess a valid letter only')
        else:
            print('Please Guess One letter at a time')

    def draw_phrase_banner(self):
        phrase_text = ''
        for char in self.phrase:
            if char == ' ':
                phrase_text += ' '
            elif char.upper() in self.guess_list:
                phrase_text += char
            else:
                phrase_text += '_'

        return phrase_text

    def draw_guessed_letters(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        guessed_letters_text = '# '
        for char in alphabet:
            if char in self.guess_list:
                guessed_letters_text += char
            else:
                guessed_letters_text += '*'
        guessed_letters_text += ' #'
        return guessed_letters_text

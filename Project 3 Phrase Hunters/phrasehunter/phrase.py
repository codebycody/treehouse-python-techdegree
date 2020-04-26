import random


class Phrase:

    def random_phrase(self):

        phrase_list = [
            'Be yourself everyone else is already taken',
            'No one can make you feel inferior without your consent',
            'Success usually comes to those who are too busy to be looking for it',
            'It is not who you are that holds you back it is who you think you are not',
            'What the mind of man can conceive and believe the mind of man can achieve',
            'We are what we repeatedly do excellence then is not an act but a habit'
        ]

        return phrase_list[random.randint(0, len(phrase_list) - 1)]

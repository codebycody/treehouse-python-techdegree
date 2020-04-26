from phrasehunter.game import Game

if __name__ == '__main__':
    try:
        phrasehunter = Game()
        phrasehunter.start()

    except Exception as e:
        raise e

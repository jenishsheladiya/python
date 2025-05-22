# Game Score Tracker
class Game:
    def __init__(self):
        self.__score = 0

    def increase_score(self):
        self.__score += 10

    def get_score(self):
        return self.__score

g = Game()
g.increase_score()
print(g.get_score())

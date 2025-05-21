# Exam Score Validator
class Exam:
    def __init__(self):
        self.__score = 0

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score

    def get_score(self):
        return self.__score

e = Exam()
e.set_score(85)
print(e.get_score())

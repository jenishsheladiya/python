# Fitness Tracker
class Workout:
    def __init__(self, exercise, calories):
        self.exercise = exercise
        self.calories = calories

class User:
    def __init__(self, name):
        self.name = name
        self.total_calories = 0

    def do_workout(self, workout):
        self.total_calories += workout.calories
        print(f"{self.name} did {workout.exercise} and burned {workout.calories} calories.")

    def show_total(self):
        print(f"Total calories burned: {self.total_calories}")

u1 = User("Jenish")
w1 = Workout("Running", 200)
w2 = Workout("Cycling", 300)

u1.do_workout(w1)
u1.do_workout(w2)
u1.show_total()

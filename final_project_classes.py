# Final Project Classes

# User class to store information about user
class User:
    def __init__(self, fname, lname, age, height, current_weight):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.current_weight = current_weight
        self.height = height
        self.goals = {}
        self.workouts = []
        self.meals = []

    def log_exercise(self, exercise):
        self.workouts.append(exercise)

    def set_goals(self, weight_goal, calorie_goal, consistency_goal):
        self.goals['weight_goal'] = weight_goal
        self.goals['calorie_goal'] = calorie_goal
        self.goals['workout_goal'] = consistency_goal

# Exercise class to store information about exercise
class Exercise:
    def __init__(self, exercise_type, intensity, duration):
        self.exercise_type = exercise_type
        self.intensity = intensity
        self.duration = duration

# Goal class to store information about goal
class Goal:
    def __init__(self, weight_goal, calorie_goal, consistency_goal):
        self.weight_goal = weight_goal
        self.calorie_goal = calorie_goal
        self.consistency_goal = consistency_goal

# Meal class to store information about meal
class Meal:
    def __init__(self, meal_type, food, meal_calories):
        self.meal_type = meal_type
        self.food = food
        self.meal_calories = meal_calories
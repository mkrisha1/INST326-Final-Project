import re
import sys
import pandas as pd
import matplotlib.pyplot as plt

# User class to store information about user
class User:
    """ Represents a user in the tracking system.

        Attributes:
            fname (str): The user's first name.
            lname (str): The user's last name.
            age (int): The user's age.
            height (int): The user's height in inches.
            current_weight (int): The user's current weight in pounds.
            goals (dict): A dictionary that stores the user's goals (ex. weight, calorie intake, workout consistency).
            workouts (list): A list of Exercise objects representing the user's logged workouts.
            meals (list): A list of Meal objects representing the user's logged meals.
    """
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
        """ Logs an exercise by adding it to the user's workout list.

            Args:
                exercise (Exercise): An Exercise object representing an exercise that is logged.
        """
        self.workouts.append(exercise)

    def set_goals(self, weight_goal, calorie_goal, consistency_goal):
        """ Sets the user's fitness and nutrition goals.

            Args:
                weight_goal (int): The user's weight goal.
                calorie_goal (int): The user's daily calorie intake goal.
                consistency_goal (int): The user's goal as to how many times they want to work out per week.
        """
        self.goals['weight_goal'] = weight_goal
        self.goals['calorie_goal'] = calorie_goal
        self.goals['workout_goal'] = consistency_goal

# Exercise class to store information about exercise
class Exercise:
    """ Represents an exercise session.

        Attr:
            exercise_type (str): The type of exercise performed (ex. cardio, legs, etc.).
            intensity (str): The exercise's intensity level on a scale of 1 to 10.
            duration (str): How long the workout was for in minutes.
    """
    def __init__(self, exercise_type, intensity, duration):
        self.exercise_type = exercise_type
        self.intensity = intensity
        self.duration = duration

# Goal class to store information about goal
class Goal:
    """ Represents a set of fitness and nutrition goals for a user.

        Attr:
            weight_goal (int): The user's weight goal in pounds.
            calorie_goal (int): The user's daily calorie intake goal.
            consistency_goal (int): The user's goal as to how many workouts they want to complete each week.
    """
    def __init__(self, weight_goal, calorie_goal, consistency_goal):
        self.weight_goal = weight_goal
        self.calorie_goal = calorie_goal
        self.consistency_goal = consistency_goal

# Meal class to store information about meal
class Meal:
    """ Represents a meal and its associated nutritional information.

        Attr:
            meal_type (str): The type of meal (ex. breakfast, lunch, dinner, snack).
            food (str): The food type of food eaten for the specific meal.
            meal_calories (int): The total calorie intake of the meal.
    """
    def __init__(self, meal_type, food, meal_calories):
        self.meal_type = meal_type
        self.food = food
        self.meal_calories = meal_calories
        
# Function for user to input their information when opening the app
def open_app():
    """ Prompts the user to input their information when opening the app including first and last name, age
        height, and current weight. It verifies the correctness of the input and returns an initialized
        User object with the inputed details.
    
        Returns:
            User: A User object initialized with the input information.
    """
    while True:
        fname = input("Please enter your first name: ")
        lname = input("Please enter your last name: ")
        age = input("Please enter your age: ")
        height = input("Please enter your height in inches: ")
        current_weight = input("Please enter your current weight in pounds: ")

        print(f"\nYou entered:\nFull Name: {fname} {lname}\nAge: {age}\nHeight: {height}\nCurrent Weight: {current_weight}\n")

        while True:
            confirm = input("Is this information correct? (y/n): ").strip().lower()
            try:
                if confirm not in ['y', 'n']:
                    raise ValueError("Invalid input. Please enter 'y' for yes or 'n' for no.")
                if confirm == 'y':
                    break
                elif confirm == 'n':
                    print("\nPlease input your information again.\n")
                    break
            except ValueError as ve:
                print(ve)

        if confirm == 'y':
            break

    user_info = User(fname, lname, int(age), int(height), int(current_weight))
    return user_info

# Function to read user information from a file
def read_user_info(filename):
    """ Reads user information from a given CSV file and reads and initializes a user object using the file's information.

        Args:
            filename (str): The CSV file's path that has the user information.

        Returns:
            User: An initialized User object with the data from the given file, or None if no valid user information is found.
    """
    pattern = r'^(/[^/ ]*)*/[^/ ]+\.csv$'
    
    while True:
        filename = input("Please enter the correct pathname to your CSV file: ").strip()

        if re.match(pattern, filename):
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines):
                        if i == 0:  # This skips the first line in the CSV file (header)
                            continue
                        user_data = line.strip().split(',')
                        if len(user_data) == 5:
                            fname, lname, age, height, weight = user_data
                            user_info = User(fname, lname, int(age), int(height), int(weight))

                            # Print out the user's information to verify correctness
                            print(f"\nUser Information:\nFirst Name: {user_info.fname}\nLast Name: {user_info.lname}\nAge: {user_info.age}\nHeight: {user_info.height} inches\nWeight: {user_info.current_weight} lbs\n")


                            return user_info
                    print("No valid user information found in the file.")
            except FileNotFoundError:
                print(f"Error: The file '{filename}' was not found. Please try again.")
            except IOError:
                print(f"Error: Could not read the file '{filename}'. Please try again.")
        else:
            print(f"Error: The file '{filename}' is not a valid CSV file. Please provide a file ending with '.csv'.")

        print("Please try again.")

# Function to calculate BMI
def calculated_bmi(bmi_weight, bmi_height):
    """ Calculates and prints the Body Mass Index (BMI) based on the user's weight and height.

        Args:
            bmi_weight (int): The user's current weight in pounds.
            bmi_height (int): The user's height in inches.
    """
    bmi = round(bmi_weight / (bmi_height ** 2) * 703, 1)
    print(f"Your current calculated BMI is {bmi}")

# Function to log exercise
def log_track_exercise(user):
    """ Allows the user to log their exercises by inputting the type, intensity, and duration of the workout.
        The function continues to ask if the user wants to log additional exercises until the user says no. Then
        prints a summary of all the logged workouts.

        Args:
            user (User): The User object representing the user logging the exercise.
        """
    while True:
        exercise_type = input('Enter the type of exercise you completed: ')
        intensity = input('Enter the intensity level of your exercise on a scale of 1 to 10: ')
        duration = input('How long did you workout for? (minutes): ')
        log = Exercise(exercise_type, intensity, duration)
        user.log_exercise(log)
        print('Your exercise has been successfully logged!')

        while True:
            add_workout = input("Do you want to log another workout? (y/n): ").strip().lower()
            try:
                if add_workout not in ['y', 'n']:
                    raise ValueError("Invalid input. Please enter 'y' for yes or 'n' for no.")
                if add_workout == 'n':
                    break
                elif add_workout == 'y':
                    break
            except ValueError as ve:
                print(ve)
        
        if add_workout == 'n':
            break

    print("\nYour Workouts:")
    for workout in user.workouts:
        print(f"Workout: {workout.exercise_type}, Intensity: {workout.intensity}, Duration: {workout.duration} minutes")
    print()

# Function to set goal
def input_goal(user):
    """ Cues the user to input their weight, calorie intake, and workout goals, then logs these goals.

        Args:
            user (User): A User class instance of where the goals will be stored.
    """
    weight_goal = int(input("Enter your weight goal (lb): "))
    calorie_goal = int(input("Enter your daily calorie intake goal: "))
    workout_goal = int(input("How many times do you want to work out per week? "))
    user.set_goals(weight_goal, calorie_goal, workout_goal)
    print('Your goals have been successfully logged!')

# Function to log meal and calories eaten
def calories_and_meal(user):
    """ Function that logs muliple meal information, calculates the total calories consumed, and displays a bar graph summary.

        Args:
            user (User): A User class instance of where meals will be logged.            
    """
    total_calories = 0

    while True:
        try:
            meal_type = input("Was your meal a breakfast, lunch, dinner, or snack?: ").strip().lower()
            if meal_type not in ['breakfast', 'lunch', 'dinner', 'snack']:
                raise ValueError("Invalid meal type. Please enter breakfast, lunch, dinner, or snack.")
            food = input(f"What did you have for {meal_type}? ")
            calories = int(input(f"Enter the total calories of your {meal_type}: "))
            total_calories += calories
            user.meals.append(Meal(meal_type, food, calories))
            print('Your meal(s) have been successfully logged!')
            
            add_meal = input("Do you want to log another meal? (y/n): ").strip().lower()
            if add_meal == 'n':
                break
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An error occurred: {e}")

    print("\nToday's Meals:")
    for meal in user.meals:
        print(f"Meal: {meal.meal_type}, Food: {meal.food}, Calories: {meal.meal_calories}")
    print(f"Total calories: {total_calories}\n")

    # Plots calories on bar graph for each meal
    meals_df = pd.DataFrame([vars(meal) for meal in user.meals])
    meals_df.groupby('meal_type')['meal_calories'].sum().plot(kind='bar')
    plt.title('Total Calories by Meal Type')
    plt.xlabel('Meal Type')
    plt.ylabel('Total Calories')
    plt.show()

# Function to track weight progress
def track_weight_progress(user):
    """ Tracks and displays the user's progress toward their weight goal.

        Args:
            user (User): A User instance of the User class that has the weight goals and current weight.
    """
    weight_goal = user.goals.get('weight_goal')
    current_weight = user.current_weight
    if weight_goal is not None:
        pounds_to_lose_or_gain = current_weight - weight_goal
        if pounds_to_lose_or_gain > 0:
            print(f"You need to lose {abs(pounds_to_lose_or_gain)} pounds to reach your weight goal. You got this!")
        elif pounds_to_lose_or_gain < 0:
            print(f"You need to gain {abs(pounds_to_lose_or_gain)} pounds to reach your weight goal. You got this!")
        else:
            print("Congratulations! You have reached your weight goal!")
    else:
        print("Please enter a weight goal to track your progress.")

# Function to track consistency progress
def track_workout_progress(user):
    """ Tracks and shows the user's progress toward their workout consistency goal.

        Args:
            user (User): An instance of the User class that has the user's workout goals and logged workouts.
    """
    workout_goal = user.goals.get('workout_goal')
    if workout_goal is None:
        print("No workout goal set.")
        return
    
    completed_workouts = len(user.workouts)
    remaining_workouts = workout_goal - completed_workouts
    if remaining_workouts > 0:
        print(f"You need to complete {remaining_workouts} more workouts this week to meet your goal. You're almost there!")
    else:
        print("Congratulations! You've met your workout goal for the week!")
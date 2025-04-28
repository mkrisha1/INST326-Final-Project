# Main function for user interaction, run this to actually see the tracker in play.

from final_project import open_app, calculated_bmi, input_goal, log_track_exercise, calories_and_meal, track_weight_progress, track_workout_progress, read_user_info

def main():
    """The main function for the Fitness and Nutrition Tracker application that allows the tracker to run. Gives the
        user a menu driven interface that allows the user to select from a list of options to input their information,
        calculate their current BMI, set goals, log exercises and meals, and track their progress. The user must
        input their information manually or submitting a CSV file before accessing the tracker's other various features. 
    """
    user_info = None
    while True:
        print("\nWelcome to the Fitness and Nutrition Tracker!")
        print("--- Please enter your information first by selecting option 1 or option 2, then choose any option 3 through 9! ---")
        print("1. Enter user information manually")
        print("2. Enter user information by submitting a CSV file")
        print("3. Calculate Body Mass Index (BMI)")
        print("4. Set Goals")
        print("5. Log Exercise")
        print("6. Log Meals and Calorie Intake")
        print("7. Track Weight Progress")
        print("8. Track Workout Consistency Progress")
        print("9. Exit")

        # Goes to the certain function depending on what number option the user chooses
        choice = input("Please enter user data first (option 1 or 2) then choose any option 3 through 9: ").strip()

        if choice == '1':
            user_info = open_app()
            print("User information has been successfully entered!")
        elif choice == '2':
            filename = input("Please enter the CSV file pathname (please use a slash (/) to separate directories): ").strip()
            user_info = read_user_info(filename)
            if user_info:
                print("User information has been read from the file and successfully logged!")
            else:
                print("Failed to read user information from the file. Please make sure the format of your file is correct.")
        elif choice == '3':
            if user_info:
                calculated_bmi(user_info.current_weight, user_info.height)
            else:
                print("Please enter user information first by selecting option 1 or 2.")
        elif choice == '4':
            if user_info:
                input_goal(user_info)
            else:
                print("Please enter user information first by selecting option 1 or 2.")
        elif choice == '5':
            if user_info:
                log_track_exercise(user_info)
            else:
                print("Please enter user information first by selecting option 1 or 2.")
        elif choice == '6':
            if user_info:
                calories_and_meal(user_info)
            else:
                print("Please enter user information first by selecting option 1 or 2.")
        elif choice == '7':
            if user_info:
                track_weight_progress(user_info)
            else:
                print("Please enter user information first by selecting option 1 or 2.")
        elif choice == '8':
            if user_info:
                track_workout_progress(user_info)
            else:
                print("Please enter user information first by selecting option 1 or 2.")
        elif choice == '9':
            print("You are now exiting the Fitness and Nutrition Tracker. You got this!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 9.")

# Runs the main function
if __name__ == "__main__":
    main()
# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

# def print_greeting():
#     # Your code goes here. Remember to indent!
#     python_is_fun = True
#     if python_is_fun:
#         print("Python is fun!")

# # Call the function
# print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter():
#     # Your control flow logic goes here
#     letter = input('enter a letter (a-z or A-Z): ').strip()
#     if len(letter) == 1 and letter.isalpha():
#         letter_lower = letter.lower()
#         vowels = 'aeiou'
#         if letter_lower in vowels:
#             print(f'the letter {letter} is a vowel.')
#         else:
#             print(f'the letter {letter} is a consonant.')
#     else:
#         print("invalid input, please enter a single alphabetical letter.')
# # Call the function
# check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     # Your control flow logic goes here
#     voting_age = 18

#     try:
#         age = int(input('please enter your age: ').strip())
#         if age <0:
#             print('please enter a valid age')
#         elif age >= voting_age:
#             print('you are eligible to vote')
#         else:
#             print(f'you are not eligible to vote, please wait {voting_age - age} years')
#     except ValueError:
#         print('invalid input, please enter a number')    
# # Call the function
# if __name__ == '__main__':
#     check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years():
#     # Your control flow logic goes here
#     try:
#         dog_age = float(input("Input a dog's age in human years: ").strip())
#         if dog_age < 0:
#             print('please enter a valid age (non-negative number).')
#         else:
#             if dog_age <= 2:
#                 dog_years = dog_age * 10  
#             else:
#                 dog_years = 20 + (dog_age - 2) * 7  
#             print(f"the dog's age in dog years is {dog_years:.1f}.")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value.")
# # Call the function
# if __name__ == "__main__":
#     calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# def weather_advice(**kwargs):
#     # Your control flow logic goes here
#     is_cold = kwargs.get('cold', 'no').strip().lower()  
#     is_raining = kwargs.get('raining', 'no').strip().lower()  

    
#     if is_cold not in ['yes', 'no'] or is_raining not in ['yes', 'no']:
#         print("Invalid input. Please enter 'yes' or 'no'.")
#         return  

#     if is_cold == 'yes' and is_raining == 'yes':
#         print("Wear a waterproof coat.")
#     elif is_cold == 'yes' and is_raining == 'no':
#         print("Wear a warm coat.")
#     elif is_cold == 'no' and is_raining == 'yes':
#         print("Carry an umbrella.")
#     else:  
#         print("Wear light clothing.")

# if __name__ == "__main__":
#     is_cold_input = input("Is it cold? (yes/no): ").strip().lower()
#     is_raining_input = input("Is it raining? (yes/no): ").strip().lower()
#     weather_advice(cold=is_cold_input, raining=is_raining_input)

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.
   
def determine_season(**kwargs):
     # Your control flow logic goes here
    month = kwargs.get('month', '').strip().capitalize()
    day = kwargs.get('day', '').strip()

    try:
        day = int(day)
    except ValueError:
        print("Invalid day input. Please enter a valid numeric day.")
        return

    valid_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if month not in valid_months:
        print("Invalid month. Please enter a valid month abbreviation (example: Jan, Feb, Mar).")
        return

    if (month == "Dec" and day >= 21) or (month == "Jan") or (month == "Feb") or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or (month == "Apr") or (month == "May") or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or (month == "Jul") or (month == "Aug") or (month == "Sep" and day <= 21):
        season = "Summer"
    else: 
        season = "Fall"
    print(f"{month} {day} is in {season}.")

if __name__ == "__main__":
    month_input = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    day_input = input("Enter the day of the month: ").strip()
    

# Call the function
determine_season(month=month_input, day=day_input)

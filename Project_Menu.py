from datetime import datetime

print("kriagu7298 Spreadsheet Automation Menu")

menuOptions = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
]

print("Choose a number from the following options")

# This loop variable represents each menu option in the list.
for option in menuOptions:
    print(option)

# The next line retrieves the inputted option and stores into the variable called user_choice.
user_choice = input("Enter your selection: ")

if user_choice == "1" or user_choice == "2" or user_choice == "3":
    print("You selected", user_choice, "at", str(datetime.now()))
else:
    print("Error: Invalid choice selected")

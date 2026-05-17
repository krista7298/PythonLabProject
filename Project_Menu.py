from datetime import datetime

print("kriagu7298 Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called user_choice.
user_choice = input("Enter your selection: ")

print("You selected", user_choice, "at", str(datetime.now()))

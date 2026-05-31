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

# Function to convert Fahrenheit to Celsius
def convertData(tempF):
    return (tempF - 32) * 5 / 9

# Function to collect user input
def getInput():

    entryCount = int(input("How many entries are you inputting?\n"))

    for counter in range(entryCount):

        dateEntered = input("\nEnter a date:\n")

        tempF = float(input("Enter the highest temp for the inputted date:\n"))

        # Function: convertData
        # Argument: temperature in Fahrenheit
        # Returns: temperature in Celsius
        convertedTemp = convertData(tempF)

        print(f"The following was saved at {datetime.now()} :")
        print(f"{dateEntered},{tempF},{convertedTemp}")

# The next line retrieves the inputted option and stores into the variable called user_choice.
user_choice = input("Enter your selection: ")

if user_choice == "1":
    print("You selected", user_choice, "at", str(datetime.now()))
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")

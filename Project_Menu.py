from datetime import datetime

# Function to convert Fahrenheit to Celsius
def convertData(tempF):
    return (tempF - 32) * 5 / 9


# Function to insert data into the CSV file
def insertData(path, data):

    try:
        with open(path, "a") as file:
            file.write(data + "\n")

    except Exception as e:
        print("Error writing to file:", e)


# Function to display the contents of the CSV file
def viewData(path):

    try:
        print("The file", path)

        with open(path, "r") as file:
            contents = file.read()
            print(contents)

    except Exception as e:
        print("Error reading file:", e)


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

        data = f"{dateEntered},{tempF},{convertedTemp}"

        try:

            insertData("ZooData.csv", data)

            print(f"The following data was saved at {datetime.now()} :")
            print(data)

        except Exception as e:
            print("Error saving data:", e)


print("kriagu7298 Spreadsheet Automation Menu")

menuOptions = [
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
]

print("Choose a number from the following options")

for option in menuOptions:
    print(option)

user_choice = input()

if user_choice == "1":

    print("You selected", user_choice, "at", str(datetime.now()))
    getInput()

elif user_choice == "2":

    print("You selected", user_choice, "at", str(datetime.now()))
    viewData("ZooData.csv")

else:

    print("Error: The chosen functionality is not implemented yet")

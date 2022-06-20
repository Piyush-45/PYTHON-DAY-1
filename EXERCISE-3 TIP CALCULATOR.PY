# TIP CALCULATOR




print("Welcome to the tip calculator")

total_bill = int(input("What is the total bill ?\n"))
tip_value = int(input("What percentage tip would you like to give ? 10, 12, 13 or 15 \n"))
no_of_people = int(input("How many people to spilt the bill ? \n"))

bill_amount = round((total_bill + tip_value) / no_of_people)
print(f"Each person should pay: ${bill_amount}")
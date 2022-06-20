# life in weeks

age = int(input("What is your current age ? \n"))

years_remaining = 90 - age
days_remaining  = years_remaining * 365
weeks_remaining  = years_remaining * 52
months_remaining  = years_remaining * 12

print(f"you have {years_remaining} years remaining , {months_remaining} months remaining, {weeks_remaining} weeks remaining  and {days_remaining} days remaining ")



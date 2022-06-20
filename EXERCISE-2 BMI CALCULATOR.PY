#  BMI CALCULATOR

from operator import indexOf


print("For calculating the BMI plz enter the following details :")
weight = input("Enter your weight in kg - ")
height = input("enter yout height in m - ")

bmi_result = int(weight) / float(height)**2
# print("your bmi is :"  + str(bmi_result))
print("your bmi is : " "{:.2f}".format(round(bmi_result, 2))  )
c= bmi_result

# adding if and else 

if c < 18.5:
    print(f"your bmi is {c}, you are underweight")
elif c < 25:
    print(f"your bmi is  {c}, you have a normal weight ")
elif c>30:
    print(f"your bmi is  {c}, you are overweight")
    
 
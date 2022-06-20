# random module
# import random

# random_side = random.randint(0,1)
# if random_side==1:
#     print("Heads")
# else: print("Tails")



# ********* WHO WILL PAY THE BILL **********😭😭😭😭😭
import random

names = input(("enter the name of persons "))
name_in_list = names.split(" ,")
print(name_in_list)

# no_of_persons  = len(name_in_list)
# print(no_of_persons)

# # selecting randomly
# random_choice = random.randint(0, no_of_persons-1)
# person_who_will_pay_bill = names[random_choice]
# print(person_who_will_pay_bill +" Will pay the today'd bill 🤑")

# ----- ISI CODE KO ITTU SA KRKE DIKHATE HAI ------(choice ())

person_who_will_pay_bill = random.choice(name_in_list)
print(person_who_will_pay_bill +" Will pay the today's bill 🤑")



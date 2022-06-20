# pizza order exercise

print("Welcome to python pizza diliveries !")

size = input("What size pizza do you want ? S, M, or L \n")
add_pepperoni = input("Do you want to add pepperoni ? Y or N \n")
extra_cheese = input("Do you want extra cheese ? Y or N \n")
bill = 0

if size == "S" :
    bill+= 15 
    print("selected pizza is Small")
elif size == "M":
    bill+= 20
    print("selected pizza size is medium")
elif size == "L":
    bill+= 25
    print("selected pizza size is Large")


if add_pepperoni == "Y":
    if size == "S":
         bill+=2
    else:
        bill+=3


if extra_cheese == "Y":
    bill+=1


print(f"your final bill is {bill}")
    
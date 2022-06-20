# love calculator
print("Welcome to the love calculator ❤️")

boy_name = input("Enter the name of boy ")
girl_name = input("Enter the name of girl ")

combined_name = boy_name + girl_name
lower_case_string = combined_name.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e=  lower_case_string.count("e")

true = t +  r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e=  lower_case_string.count("e")

love = l + o + v + e

love_Score = str(true) + str(love)
print(love_Score)

if love_Score < str(40):
    print("DOOR HI RAHO BHAIYA EK DOOSRE SE")
elif love_Score > str(40) and love_Score< str(80):
    print("chalo chal jayega tumhara")
elif love_Score > str(90) :
    print("OMFOO MAZE AAGYE")
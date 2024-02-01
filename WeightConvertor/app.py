weight=input("Enter Weight ")

print("select unit kg or lb for the value entered")
unit=input("Enter Unit ")
print(unit)
if unit=="kg":
    print("Value in pounds "+ str(2.2*int(weight)))
elif unit=="lb":
    print("value in kg "+ str(0.45*int(weight)))

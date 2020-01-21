unam = "Jayaram"
pwd = "jay123"
i = 0
uname1 = str(input("Enter your username "))
pwd1 = str(input("Enter your password "))
while i < 3:
  if(unam == uname1 and pwd == pwd1):
    print("Valid login")
    break
  else:
    print("Invalid login")
i += 1  
sour = int(input("Enter the source "))
dest = int(input("Enter the destination "))
typ = str(input("Enter the type of car "))
while( typ == "mini" or typ == "sedan" or typ == "xuv" or typ == "premium"):
  if(typ == "mini"):
    cmodel = input("Select your model: 1. indigo 2. indica 3.zen ")
    break
  elif(typ == "sedan"):
    cmodel = input("Select your model: 1. Dzire 2. city 3.verna ")
    break
  elif(typ == "xuv"):
    cmodel = input("Select your model: 1. ecosport 2. duster 3.scorpio ")
    break
  elif(typ == "premium"):
    cmodel = input("Select your model: 1. benz 2. bmw 3.audi ")
    break
  else:
    print("invalid type")
  
if(dest < 6):
  if(typ == "mini"):
    price = 50
  elif(typ == "sedan"):
    price = 60
  elif(typ == "xuv"):
    price = 75
  else:
    price = 100
elif(dest > 5):
  if(typ == "mini"):
    price = (50 + ((dest - 5)*9))
  elif(typ == "sedan"):
    price = (60 + ((dest - 5)*11))
  elif(typ == "xuv"):
    price = (75 + ((dest - 5)*13))
  else:
    price = (100 + ((dest - 5)*18))
else:
  pass
print("Bill ")
print("Name: ",unam)
print("Total price: ",price)
print("Type: ",typ)
print("Model: ",cmodel)
print("Thank you for using jack cabs!")

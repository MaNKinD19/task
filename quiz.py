a={1:"Solve 1+1",2:"Solve 10-3",3:"Solve 5*5",4:"solve 15/3"}
sc=0
b=len(a)
for i in range(1,b+1):
  print(i,a[i])
w=int(input("Answer for 1 "))
if (w==2):
  sc=sc+5
  print("Your answer is correct")
else:
    print("Your answer is wrong")
x=int(input("Answer for 2 "))
if x==7:
  sc=sc+5
  print("Your answer is correct")
else:
    print("Your answer is wrong")
y=int(input("Answer for 3 "))
if y==25:
  sc=sc+5
  print("Your answer is correct")
else:
    print("Your answer is wrong")
z=int(input("Answer for 4 "))
if z==5:
  sc=sc+5
  print("Your answer is correct")
else:
    print("Your answer is wrong")
print("FinalScore: ",sc)

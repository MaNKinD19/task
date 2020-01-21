from random import randint
n=randint(0,9)
i=0
while(i<5):
    num=int(input("guess number"))
    if num == n:
        print(" correct",n)
        break
    else:
        print("Wrong ")
        print("Attempt remaining : ",4-i)
    i=i+1

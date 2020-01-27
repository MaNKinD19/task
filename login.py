import getpass
import random
name=''
mid=''
d={}
def reg():
    c=0
    acc=list(range(1000,9999))
    random.shuffle(acc)
    name=input("Enter your name :")
    while(c<3):
        mid=input("Enter maid id :")
        if  "@gmail.com" in mid:
            if mid!="@gmail.com":
                print("Valid Id")
                break
        else:
            print("Invalid Id")
            c=c+1
            
    a=acc.pop()
    print("Account number :",a)
    pwd=getpass.getpass("Enter  password :")
    d.update({a:pwd})
    print("Account registeed succesfully!!!")
reg()
def login():
    uno=input("Enter Account number ")
    upwd=getpass.getpass("Enter password")
    if uno in d and upwd == d[uno]:
        print("Login succesfully")
        
    else:
        print("Try again")
login()

    

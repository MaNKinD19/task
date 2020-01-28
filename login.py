import getpass
import random
name=''
mid=''
d={}
det={}
def reg():
    c=0
    f=open("Bank.txt","w+")
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
    c=0
    while c<3:
        bal=float(input("Enter balance amount(>5000) "))
        if bal<5000:
            print("Minimum balance Required")
            c=c+1
        else:
            print("Amount credited succesfully!!!")
            break
    d.update({a:pwd})
    det.update({a:[name,mid,bal,pwd]})
    f.write("%s\r\n"%det)
    print("Account registeed succesfully!!!")
    f.close()
reg()
def dep():
    f.open("Bank.txt","r+")
    u=eval(f.read())
    damt=float(input("Enter Amount"))
    
    
def login():
    c1=0
    while c1<3:
        uno=int(input("Enter Account number "))
        upwd=getpass.getpass("Enter password ")
        if uno in d and upwd == d[uno]:
            print("Login succesfully")
            break
        else:
            print("Try again")
            c1=c1+1
login()

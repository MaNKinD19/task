import getpass
import random
name=''
mid=''
d={}
det={}
#getlist returns dictionary values
def getList(dict): 
    return dict.keys() 
#reg performs registration
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

#dep function deposits amount
def dep(userid):
    f.open("Bank.txt","r+")
    u=eval(f.read())
    damt=float(input("Enter Amount"))
    if damt<500 and damt>50000:
        print("Limit exceeded")
    else:
        print("Deposited succesfully")
        bal=bal+damt
    f=open("Bank.txt","w+")
    u[userid][2]=bal    
    f.write("%s\r\n"%u)
    f.close()
    
    #wdraw function withdraws amount
def wdraw(userid):
    f.open("Bank.txt","r+")
    v=eval(f.read())
    wamt=float(input("Enter Amount"))
    if wamt<500 and wamt>50000:
        print("Limit exceeded")
    elif (bal-wamt)<5000:
        print("exceeding Minimum Balance")
    else:
        print("Withdrawl succesful")
        bal=bal-wamt
    f=open("Bank.txt","w+")
    u[userid][2]=bal    
    f.write("%s\r\n"%u)
    f.close()
    
#bcheck function checks balance
def bcheck(userid):
    f.open("Bank.txt","r+")
    w=eval(f.read())
    bal=r[userid][2]
    print("Balance :",bal)
    f.close()
    
#login perform login function
def login():
    c1=0
    c2=0
    f=open("Bank.txt","r+")
    x=eval(f.read())
    l=getList(x)
    uno=int(input("Enter Account number "))
    upwd=getpass.getpass("Enter password ")
    for i in l:
        while c1<3:
        if uno i== det and upwd == det[i][3]:
            print("Login succesfully")
            break
        else:
            print("Try again")
            c1=c1+1
    
    while c2<3:
        ch=int(input("""Enter your choice 1. Deposit
        2. Withdraw
        3. Check Balance"""))
        if ch==1:
            dep(uno)
        elif ch==2:
            wdraw(uno)
        elif ch==3:
            bcheck(uno)
        else:
            print("Invalid Choice")
            c=c+1
    
j='y'
Print("**************Basic Bank Welcomes You!!!*******************")
while(j=='y'):
    ch1=int(input("Enter your choice 1. register 2. Login"))
    if ch==1:
        reg()
    elif ch==2:
        login()
    else:
        print("Invalid choice")
    j=input("Do you want to continue?(y/n")
    

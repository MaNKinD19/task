f=open("sum.txt","w+")
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = int(input("Enter choice(1/2/3/4): "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
f.write("Choice%d\r\n"%(choice))
f.write("First number%d\r\n"%(num1))
f.write("Second number%d\r\n"%(num2))
if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))
   f.write("Sum%d\r\n"%(add(num1,num2)))
elif choice == 2:
   print(num1,"-",num2,"=", subtract(num1,num2))
   f.write("Difference%d\r\n"%(subtract(num1,num2)))
elif choice == 3:
   print(num1,"*",num2,"=",multiply(num1,num2) )
   f.write("Product%d\r\n"%(multiply(num1,num2)))
elif choice == 4:
   print(num1,"/",num2,"=",divide(num1,num2) )
   f.write("Quotient%d\r\n"%(divide(num1,num2)))
else:
   print("Invalid input")
print(f.read())

f.close()

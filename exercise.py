
#Calculator
"""
print("Hello and welcome to this simple calculator\n ")
ch=1
while(ch==1):
    try:
        a=float(input("Enter the Value of A: "))
        b=float(input("Enter the Value of B: "))
        operation=input('Enter operation: ')
    except ValueError as error:
            print("Is not valid input:",error)  
    else:
            if operation=='+':
                print(a,"+",b,"=",a+b)
            elif operation=='-':
                print(a,"-",b,"=",a-b)             
            elif operation=='*':
                print(a,"*",b,"=",a*b)
            elif operation=='/':
                try:
                    print (a,"/",b,"=",a/b)
                except ZeroDivisionError as error:
                      print ("Can't divide to zero:",error)
            else:
                      print("Enter correct operation!")
    finally:
           print("Thank you for using this calculator!")
"""
    
#Random     
"""
import random
count = 0
while count<3:
    num1 = int(input("Enter number: "))
    num2 = random.randint(0, 100)
    if num1  == num2:
        print('Congratulations')
    else:
        print("Try again")
        count+=1
print("Number is {}".format(num2))
"""


#Password
"""a=input()
if(len(a)>=8 and len(a)<=13):
    print('Successfully')
else:
    print('Incorrect password!!!')"""
    

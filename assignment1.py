#1. Write a python program for the following: – Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it.

x=input()
x=x.replace('py','')
print(x)
r=''
for i in x:
    r=i+r
print(r)

#– Take two numbers from user and perform at least 4 arithmetic operations on them.
num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')  
  
# Addition  
sum = float(num1) + float(num2)  
# Subtraction 
min = float(num1) - float(num2)  
# Multiplication  
mul = float(num1) * float(num2)  
#Division  
div = float(num1) / float(num2)  
#Modulus
mod=float(num1) % float(num2) 
#Exponent
expo=float(num1) ** float(num2)
# Display the Addition 
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div)) 
#Display the Modulus
print('The modulus of {0} and {1} is {2}'.format(num1, num2, mod))
#Display the Exponent
print('The exponent of {0} and {1} is {2}'.format(num1, num2, expo))




#2. Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.

str = "I love playing with python."
 
# replacing python with pythons.
str = str.replace('python', 'pythons')
print("Modified string : ")
print(str)


#3. Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class.

print("Enter Marks Obtained in Neural Network Deep Learning: ");

markOne = int(input())

if markOne <= 100: 

    if markOne>=90 and markOne<=100:

        print("Your Grade is A")

    elif markOne>=80 and markOne<=89:

        print("Your Grade is B")

    elif markOne>=70 and markOne<=79:

        print("Your Grade is C")

    elif markOne>=60 and markOne<=69:

        print("Your Grade is D")

    elif markOne>=0 and markOne<=60:

        print("Your Grade is F")
else:
    print("Invalid Input!")


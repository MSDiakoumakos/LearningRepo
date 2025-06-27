#Importing the function library
from functions import *

#Requesting user input for the numbers
def get_user_input():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    
    return x,y

#calling the functions from the library
def display_results(x,y):
    result=addition(x,y)
    print(f"{x} + {y} = {result}")
    result=subtraction(x,y)
    print(f"{x} - {y} = {result}")
    result=multiplication(x,y)
    print(f"{x} * {y} = {result}")
    result=division(x,y)
    print(f"{x} / {y} = {result}")
    result=modulus(x,y)
    print(f"{x} % {y} = {result}")
    result=power(x,y)

if __name__ == "__main__":
    print("=== Math Calculator ===")
    x,y=get_user_input()
    display_results(x,y)
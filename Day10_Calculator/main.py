from sympy import re, sec
import art
from replit import clear

print(art.logo)


status = 'n'

result = 0

def calculate(first_number, operation, second_number):
  if(operation == '+'):
    return first_number + second_number
  elif(operation == '-'):
    return first_number - second_number
  elif(operation == '*'):
    return first_number * second_number
  elif(operation == '/'):
    return first_number / second_number
  


while True:
  
  if(status == 'n'):
    first_number = int(input("What is the first number?: "))
    print("""
    +
    -
    *
    /
    """)
    operation = input("Pick an operation: ")
    second_number = int(input("What is the next number?: "))
  else:
    first_number = result
    print("""
    +
    -
    *
    /
    """)
    operation = input("Pick an operation: ")
    second_number = int(input("What is the next number?: "))

  result = calculate(first_number, operation, second_number)
  print(f"Result is : {result}")
  status = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

  if(status == 'n'):
    clear()

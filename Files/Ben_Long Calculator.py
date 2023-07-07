# Calculator

import math

def main() :
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    def exponent(x, y):
        return x ** y
    def squareroot(x):
        return math.sqrt(x)
          
    print("Select Operation")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exponent")
    print("6. squareroot")
    
    while True:
        choice = input("Select Operation(1/2/3/4/5/6): ")
      
        if choice in ('1', '2', '3', '4', '5'):

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
               
            except ValueError : 
                print("Invaild input, Please enter a number: ") 
                continue
        elif choice == ('6'):
            while True:
                try:
                    num1 = float(input("Enter first numer: "))
                    break
                except ValueError :
                    print("invalid input, Please enter a number: ")
                continue
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            print(num1, "**", num2, "=", exponent(num1, num2))
            
        elif choice == '6':
            print(num1, math.sqrt, "=", squareroot(num1))
 
        next_calculation = input("Do you want to preform another calculation? (yes/no): ")
        if next_calculation == "no" :
            break
        else:
            print("Input not valid")
            
            
main()
        
            
            
            
        
            
    
           
        

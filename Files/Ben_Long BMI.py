# Body Mass Calculator

import math

def main() :
    print("This calculates your BMI by using your height and weight")
    print("Select if you will use meters and kilograms or inches and pounds")
    print("1. cm and kilograms")
    print("2. inches and pounds")
    
    while True:
        choice = input("Selective measurment method(1/2): ")
        
        if choice in ('1'):
            
            try:
                height2 = float(input("Enter your height, in meters, here: "))
                weight2 = float(input("Enter your weight, in kilograms, here: "))
                bmi2 = weight2 // (height2 ** 2)
                print("Your BMI is", bmi2)
                print(" A BMI from 0 to 19 is underweight, 19 through 24 is healthy, and 25 and everything over is overweight")
            except ValueError :
                print("Invalid Input. Nice try pal, now please enter a number: ")
                continue    
        elif choice in ('2'):
            
            try: 
                height = float(input("Enter your height, in inches, here: "))
                weight = float(input("Enter your weight, in pounds, here: "))
                bmi = weight / (height ** 2) * 703
                print("Your BMI is", bmi)
                print(" A BMI from 0 to 19 is underweight, 19 to 24 is healthy, and 24 and everything over is overweight")
            except ValueError :
                print("Invalid Input. Nice try pal, now please enter a numer: ")
                continue
        else:
            print("Please enter a valid choice- 1 or 2")

main()

                    
        
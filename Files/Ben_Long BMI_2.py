# Ben_Long BMI_2

import math

output = ["Enter Your height", "Enter your weight", "Your BMI is", "A BMI from 0 to 19 is underweight, 19 through 24 is healthy, and 25 and everything over is overweight", "Invalid Input. Nice try pal, now please enter a number, and it cant be zero: "]

def main() :
    print("This calculates your BMI by using your height and weight")
    print("Select if you will use meters and kilograms or inches and pounds")
    print("1. cm and kilograms")
    print("2. inches and pounds")
    
    while True:
        choice = input("Selective measurment method(1/2): ")
        
        if choice in ('1'):
            
            try:
                height2 = float(input(output[0] + " in meters, here: "))
                weight2 = float(input(output[1] + " in kilograms, here: "))
                bmi2 = weight2 // (height2 ** 2)
                print(output[2], bmi2)
                print(output[3])
            except ValueError :
                print(output[4])
                continue    
        elif choice in ('2'):
            
            try: 
                height = float(input(output[0] + " in inches, here: "))
                weight = float(input(output[1] + " in pounds, here: "))
                bmi = weight / (height ** 2) * 703
                print(output[2], bmi)
                print(output[3])
            except ValueError :
                print(output[4])
                continue
        else:
            print("Please enter a valid choice- 1 or 2")

main()

                    
        
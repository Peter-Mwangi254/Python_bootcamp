#!/usr/bin/python3

'''
This program calculates the Body Mass Index (BMI) based on user input for weight and height.
It provides a BMI category classification: Underweight, Normal weight, Overweight, Obese, or Clinically obese.
'''
while True:
    try:
        #prompt the user to enter their weight in kilograms and height in meters
        weight = float (input("Enter your weight in kg:"))
        height = float (input("Enter your height in m:"))

        #check if weight and height are valid(positive) values
        if (weight <= 0 or height <= 0):
            print("Invalid input. Weight and height must be positive values.")
        else:
            # Calculate BMI and convert it to an integer.
            BMI = round(weight / (height ** 2))
            
            
            # Determine BMI category and print the result.
            if BMI > 35:
                print("You are {} ".format("Clinically obese"))
            elif BMI > 30:
                print("You are {} ".format("Obese"))
            elif BMI > 25:
                print("You are {} ".format("Overweight"))
            elif BMI > 18.5:
                print("You are {} ".format("Normal weight"))
            else:
                print("You are {} ".format("Underweight"))
    
    except ValueError:
        #Handle input errors such non numeric inputs
        print("Invalid input. Please enter valid numeric values for weight and height.")

    #ask user if they want to calculaye another BMI
    choice = input("Do you want to calculate another BMI? yes/no: ").lower

    #exit loop if the user doesnt want to calculate another BMI
    if (choice != "yes"):
        break 
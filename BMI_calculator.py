#!/usr/bin/python3
weight = float (input("Enter your weight in kg:"))
height = float (input("Enter your height in m:"))
BMI = round(weight) /(height) **2
BMI_int = (BMI)
if BMI_int > 35:
    print("You are {} ".format("Clinically obese"))
elif BMI_int > 30:
    print("You are {} ".format("Obese"))
elif BMI_int > 25:
    print("You are {} ".format("Overweight"))
elif BMI_int > 18.5:
    print("You are {} ".format("Normal weight"))
else:
    print("You are {} ".format("Underweight"))
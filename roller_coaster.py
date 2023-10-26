#!/usr/bin/python3
print("Welcome to the rollercoaster fiasco!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You are eligible to ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. Have a free ride on the house")
    else:
        bill = 12
        print("Adult tickets are $12.")
    take_photo = input("Do you want a photo taken? Y or N. ")
    if take_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
    
else:
    print("Sorry you need to grow taller before you ride the rollercoaster!")

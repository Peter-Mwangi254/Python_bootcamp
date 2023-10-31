#!/usr/bin/python3

'''
This script allows users to order pizzas by selecting the size, adding pepperoni, and choosing extra cheese. It calculates the total bill based on the user's choices.
'''
print('''
    And how about a slice?
                        ___
                        |  ~~--.
                        |%=@%%/
                        |o%%%/
                     __ |%%o/
               _,--~~ | |(_/ ._
            ,/'  m%%%%| |o/ /  `\.
           /' m%%o(_)%| |/ /o%%m `\
         /' %%@=%o%%%o|   /(_)o%%% `\
        /  %o%%%%%=@%%|  /%%o%%@=%%  \
       |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
       | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--'
''')
print("Welcome to Python Pizza Deliveries!")

try:
    '''
    User input for pizza size. The input is processed to remove leading/trailing spaces and convert to uppercase.
    '''

    size = input("What pizza size do you want? S, M, L? ").strip().upper()

    '''
    If the selected size is not S, M, or L, a ValueError is raised with an error message.
    '''
    if size not in ["S", "M", "L"]:
        raise ValueError("Invalid size. Please select a valid size (S, M, L).")

    '''
    User input for adding pepperoni. The input is processed to remove leading/trailing spaces and convert to uppercase.
    '''
    add_pepperoni = input("Do you want pepperoni? Y or N?").strip().upper()

    '''
    If the user's choice for pepperoni is not Y or N, a ValueError is raised with an error message.
    '''
    if add_pepperoni not in ["Y", "N"]:
        raise ValueError("Invalid choice. Please enter Y for Yes or N for No.")

    '''
    User input for adding extra cheese. The input is processed to remove leading/trailing spaces and convert to uppercase.
    '''
    
    extra_cheese = input("Do you want extra cheese? Y or N?").strip().upper()

    '''
    If the user's choice for extra cheese is not Y or N, a ValueError is raised with an error message.
    '''

    if extra_cheese not in ["Y", "N"]:
        raise ValueError("Invalid choice. Please enter Y for Yes or N for No.")

    bill = 0


    '''
    Calculate the base cost of the pizza based on the selected size.
    '''
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    else:
        bill +=25

    '''
    If the user wants pepperoni, additional costs are added based on the pizza size.
    '''

    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    '''
    If the user wants extra cheese, an additional cost of 1 is added to the bill.
    '''

    if extra_cheese == "Y":
        bill += 1

    '''
    Display the final bill to the user.
    '''

    print(f"Your final bill is ${bill}")

except ValueError as e:
    '''
    Handle ValueError exceptions by displaying the error message to the user.
    '''
    print(f"Error: {e}")
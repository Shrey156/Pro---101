import random

dice_list = {
    1:'[-----]\n[     ]\n[  0  ]\n[     ]\n[-----]',
    2:'[-----]\n[     ]\n[0   0]\n[     ]\n[-----]',
    3:'[-----]\n[     ]\n[0 0 0]\n[     ]\n[-----]',
    4:'[-----]\n[0   0]\n[     ]\n[0   0]\n[-----]',
    5:'[-----]\n[0   0]\n[  0  ]\n[0   0]\n[-----]',
    6:'[-----]\n[0   0]\n[0   0]\n[0   0]\n[-----]',
    }

loop=True
while loop:
    user_input = input("press 'y' to roll the dice or 'n' to exist : ")
    if user_input=='y':
        dice_num=random.randint(1,6)
        print(dice_list[dice_num])
    else:
        loop=False

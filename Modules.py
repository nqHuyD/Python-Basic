# import WelcomeModule
# from WelcomeModule import welcome
#
# welcome()
#
# WelcomeModule.yell()
#
#
# from ecommerce.shipping import calc_shipping
#
# calc_shipping()

import random


for i in range(3):
    print(random.randint(10,20))


# members = ['Jonj','asdads','asdasd']
#
# leader = random.choice(members)
#
# print(leader)


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second

dice = Dice()
print(dice.roll())

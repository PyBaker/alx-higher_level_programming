#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, int(str(number)[0]+str(number)[-1])))
elif number == 0:
    print("Last digit of {} is {} and is 0"
          .format(number, int(str(number)[-1])))
else:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, int(str(number)[-1])))

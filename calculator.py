# CODE IS FROM https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3

import math

def calculator():
 #while(1):
    operation = input('''
Please type in the math operation you would like to complete:
===========================
+ for addition
- for subtraction
* for multiplication
/ for division
sqrt for squareroot
degtorad for Degree to Radian Conversion
radtodeg for Radian to Degree Conversion
pi/ - Number 1 / pi
pi* - Number 1 * pi
fact - Factorial of a no1
q for exit
===========================
Enter operator: ''')
    if operation == 'q':
        print('Bye, bye!')
        exit()
    number_1 = float(input('Please enter the first number: '))
    if operation =='degtorad':
        print('{} deg converted to ='.format(number_1),end='')
        print(math.radians(number_1),'radians')
    elif operation =='fact':
        print("{}'s factorial is {}".format(number_1,math.factorial(number_1)))

    elif operation =='radtodeg':
        print('{} rad converted to ='.format(number_1),end='')
        print(math.degrees(number_1),'degrees')
    elif operation =='sqrt':
        print('{} square root = '.format(number_1), end='')
        print(math.sqrt(number_1))
    elif operation == 'pi/':
            print('{} / pi = '.format(number_1), end='')
            print(number_1 / math.pi)
    elif operation == 'pi*':
            print('{} * pi = '.format(number_1), end='')
            print(number_1 * math.pi)
        
    elif operation != 'sqrt' or 'degtorad' or 'radtodeg' or 'pi/' or 'pi*':
        number_2 = int(input('Please enter the second number: '))
        if operation == '+':
            print('{} + {} = '.format(number_1, number_2), end='')
            print(number_1 + number_2)
        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2), end='')
            print(number_1 - number_2)

        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2), end='')
            print(number_1 * number_2)

        elif operation == '/':
            print('{} / {} = '.format(number_1, number_2), end='')
            print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')


def addition(number_1, number_2):

  sum = number_1 + number_2
  return sum

#calculator()
#addition(3,5)
#!/usr/bin/env python

from brain_games.cli import welcome_user
 

import prompt
import random


def games(n):
    if n == 0:
        return 1
    if game() == 0:
        return 0
    return(games(n-1))

def nod(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a+b)
def game():
    random_valueA = random.randint(1, 200)
    random_valueB = random.randint(1, 200)  
    
       
    print('Question:{} {}'.format(random_valueA,random_valueB))
    answer = prompt.string('Your answer:')
    true_answer=nod(random_valueA,random_valueB)
    if int(answer) == true_answer:
        print('Correct!')
        return 1
    print(answer + "  is wrong answer ;(. Correct answer was '{}'.".format(true_answer))
    return 0


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    if games(3) == 1:
        print('Congratulations, {}!'.format(name))
    else: 
        print("Let's try again, {}!".format(name))



if __name__ == '__main__':
    main()

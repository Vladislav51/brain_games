#!/usr/bin/env python

from brain_games.cli import welcome_user
 

import prompt
import random


def games(n):
    if n == 0:
        return 1
    if even() == 0:
        return 0
    return(games(n-1))


def even():
    random_value = random.randint(1, 99)
    print('Question:', random_value)
    answer = prompt.string('Your answer:')
    if random_value % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    if answer == true_answer:
        print('Correct!')
        return 1
    print(answer + "  is wrong answer ;(. Correct answer was '{}'.".format(true_answer))
    return 0


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if games(3) == 1:
        print('Congratulations, {}!'.format(name))
    else: 
        print("Let's try again, {}!".format(name))



if __name__ == '__main__':
    main()

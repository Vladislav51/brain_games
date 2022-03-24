#!/usr/bin/env python

from brain_games.cli import welcome_user
import prompt
import random


def games(n):
    if n == 0:
        return 1
    if calc() == 0:
        return 0
    return(games(n - 1))


def calc():
    random_valueA = random.randint(1, 25)
    random_valueB = random.randint(1, 25)
    random_sign = random.randint(1, 3)
    if random_sign == 1:
        signString = '+'
        true_answer = random_valueA + random_valueB
    if random_sign == 2:
        signString = '*'
        true_answer = random_valueA * random_valueB
    else:
        signString = '-'
        true_answer = random_valueA - random_valueB
    print('Question:{} {} {}'.format(random_valueA, signString, random_valueB))
    answer = prompt.string('Your answer:')
    if int(answer) == true_answer:
        print('Correct!')
        return 1
    print("{} is wrong answer ;(. Correct answer was '{}'.".format(answer, true_answer))  # noqa: E501
    return 0


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    if games(3) == 1:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()

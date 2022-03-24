#!/usr/bin/env python

from brain_games.cli import welcome_user
import prompt
import random


def games(n):
    if n == 0:
        return 1
    if game() == 0:
        return 0
    return(games(n - 1))


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a + b)


def isprime(a, b):
    if b == 1:
        return 1
    if nod(a, b) == 1:
        return isprime(a, b-1)
    return 0


def game():
    random_valueA = random.randint(1, 200)
    print('Question:{}'.format(random_valueA))
    answer = prompt.string('Your answer:')
    if isprime(random_valueA, random_valueA - 2):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    if answer == true_answer:
        print('Correct!')
        return 1
    print("{} is wrong answer ;(. Correct answer was '{}'.".format(answer, true_answer))  # noqa: E501
    return 0


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    if games(3) == 1:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()

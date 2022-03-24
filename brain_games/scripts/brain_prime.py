#!/usr/bin/env python

from brain_games.brain_games_lib import nod, initstart
import prompt
import random


def isprime(a, b):
    if b == 1:
        return 1
    if nod(a, b) == 1:
        return isprime(a, b - 1)
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
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    initstart(rules, game)


if __name__ == '__main__':
    main()

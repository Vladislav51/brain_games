#!/usr/bin/env python

from brain_games.brain_games_lib import nod, initstart
import prompt
import random


def game():
    random_valueA = random.randint(1, 200)
    random_valueB = random.randint(1, 200)
    print('Question:{} {}'.format(random_valueA, random_valueB))
    answer = prompt.string('Your answer:')
    true_answer = nod(random_valueA, random_valueB)
    if int(answer) == true_answer:
        print('Correct!')
        return 1
    print("{} is wrong answer ;(. Correct answer was '{}'.".format(answer, true_answer))  # noqa: E501
    return 0


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    initstart(rules, game)


if __name__ == '__main__':
    main()

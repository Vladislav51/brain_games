#!/usr/bin/env python

from brain_games.brain_games_lib import initstart
import prompt
import random


def game():
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
    print("{} is wrong answer ;(. Correct answer was '{}'.".format(answer, true_answer))  # noqa: E501
    return 0


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    initstart(rules, game)


if __name__ == '__main__':
    main()

#!/usr/bin/env python

from brain_games.brain_games_lib import initstart
import prompt
import random


def game():
    random_amount = random.randint(5, 13)
    random_prog = random.randint(1, 5)
    random_miss = random.randint(1, random_amount)
    random_start = random.randint(1, 9)
    print('Question:', end=' ')
    for x in range(0, random_amount):
        if x != random_miss - 1:
            print(random_start + x * random_prog, end=' ')
        else:
            true_answer = random_start + x * random_prog
            print('...', end=' ')
    answer = prompt.string('Your answer:')
    if int(answer) == true_answer:
        print('Correct!')
        return 1
    print("{} is wrong answer ;(. Correct answer was '{}'.".format(answer, true_answer))  # noqa: E501
    return 0


def main():
    rules = 'What number is missing in the progression?'
    initstart(rules, game)


if __name__ == '__main__':
    main()

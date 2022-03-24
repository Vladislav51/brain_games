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
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    if games(3) == 1:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()

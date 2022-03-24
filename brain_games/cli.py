#!/usr/bin/env python

from brain_games.scripts.brain_games import main
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return(name)

if __name__ == '__main__':
    welcome_user()

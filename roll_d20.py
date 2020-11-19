#!/usr/bin/env python
import random


def main():
    rounds = 1
    while rounds < 11:
        print(f'Round {rounds}:\n'
              f'You rolled: {random.randint(1,20)} this round')
        if rounds == 10:
            print("\nThats all 10 rounds, thanks for playing.")
            break
        again = input('roll again y/n: ')
        if again.lower() == 'y':
            rounds += 1
        else:
            rounds = 11
            print('\nThanks for playing, good-bye.')


if __name__ == '__main__':
    main()

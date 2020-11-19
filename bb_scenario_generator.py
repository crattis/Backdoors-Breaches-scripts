#! /usr/bin/env python

import random


def select_deck(max):
    return random.randint(1, max)


def procedure_deck():
    x = 10
    while x > 6:
        print(f'Select card number {select_deck(x)} from the Procedures deck.')
        x -= 1
    return


def main():
    print("Break the deck in to its six colored parts. Shuffle each sub-deck.")
    print(f'Select card number {select_deck(10)} from the Initial Compromise deck.')
    print(f'Select card number {select_deck(7)} from the Pivot and Escalate deck.')
    print(f'Select card number {select_deck(9)} from the Persistence deck.')
    print(f'Select card number {select_deck(6)} from the C2 and Exfil deck.')
    procedure_deck()


if __name__ == '__main__':
    main()

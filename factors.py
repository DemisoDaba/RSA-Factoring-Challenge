#!/usr/bin/python3

import sys

def factorize(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            factors.append((i, number // i))
            number //= i
    if number > 1:
        factors.append((number, 1))
    return factors

def main():
    if len(sys.argv) < 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        number = int(number)
        factor_pairs = factorize(number)
        for factor_pair in factor_pairs:
            p, q = factor_pair
            print(f"{number} = {p} * {q}")

if __name__ == "__main__":
    main()


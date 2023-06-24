#!/usr/bin/python3

import sys
import math

def factorize(number):
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factor_pairs = factorize(number)
            for pair in factor_pairs:
                p, q = pair
                print(f"{number}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)

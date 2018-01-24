# Question 8

"""
    Write a program that generates random 4 digits
    number of 0s and 1s and convert the generated number to base 10.
"""

import random


def main():
    def random_01s(digits):
        c = 0
        num_array = []
        while c < digits:
            rand_btw = random.choice('01')
            num_array.append(rand_btw)
            c += 1
        the4digits = num_array[0] + "" + num_array[1] + "" + num_array[2] + "" + num_array[3]
        return "The 'base 10' of the value " + the4digits + " is " + str(int(the4digits, 2)) + "."

    print(random_01s(4))


if __name__ == "__main__":
    main()

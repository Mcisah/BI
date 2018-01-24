# Question 9

"""
    Write a program to sum the first 50 fibonacci sequence.
"""


def main():
    pass

    def fib(n):
        a, b = 1, 1
        for i in range(n - 1):
            a, b = b, a + b
        return a

    def result_output(seq=50):
        print("The sum of the first " + str(seq) + " fibonacci sequence  is " + str(fib(seq)))

    c = 0
    while c == 0:
        choice = input("Would you like to input a sequence number? (Default Sequence: 50) \n(Y/N): ")
        if choice == "Y" or choice == "N":
            if choice == "Y":
                the_seq = input("Sequence: ")
                result_output(int(the_seq))
                break
            elif choice == "N":
                result_output()
                break
        else:
            print("Wrong Input")


if __name__ == "__main__":
    main()

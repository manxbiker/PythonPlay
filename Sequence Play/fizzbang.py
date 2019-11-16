"""Outputs the sequence 1, 2, Fizz, 4, Bang, Fizz, ...
Where any number divisible by 3 outputs 'Fizz',
any number divisible by 5 outputs 'Bang',
and any number divisible by both outputs 'FizzBang'"""

def FizzBang(*args):
    #detect the number of arguments for (start, end), or just (end)
    if len(args) >= 2:
        start = args[0]
        end = args[1]
    elif len(args) ==1:
        start = 1
        end = args[0]

    for n in range(start, end):
        if n % 15 == 0:
            print("FizzBang")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Bang")
        else:
            print(n)


def main():
    #Simple case 1 to 20
    FizzBang(21)
    #Higher range 100 to 125
    FizzBang(100, 126)

if __name__ == "__main__":
    main()

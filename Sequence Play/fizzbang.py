"""Outputs the sequence 1, 2, Fizz, 4, Bang, Fizz, ...
Where any number divisible by 3 outputs 'Fizz',
any number divisible by 5 outputs 'Bang',
and any number divisible by both outputs 'FizzBang'"""

def FizzBang(start, end):
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
    FizzBang(1,21)
    #Higher range 100 to 125
    FizzBang(100, 126)

if __name__ == "__main__":
    main()
    
#fizz buzz as I originally coded it

def fizzbuzz(n):
    if n%15 == 0:
        return("Fizz Buzz")
    elif n%3 == 0:
        return("Fizz")
    elif n%5 == 0:
        return("Buzz")
    else:
        return(n)

for n in range(1,31):
    print(fizzbuzz(n))

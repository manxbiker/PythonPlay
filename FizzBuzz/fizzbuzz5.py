#fizz buzz inspired by 
#https://www.youtube.com/watch?v=FyCYva9DhsI at 19:58
#found at 
#https://codereview.stackexchange.com/questions/763/two-fizzbuzz-solutions 

def fizzbuzz(n):
    return "Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or n

for n in range(1,31):
    print(fizzbuzz(n))

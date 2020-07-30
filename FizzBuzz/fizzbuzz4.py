#fizz buzz inspired by 
#https://www.youtube.com/watch?v=FyCYva9DhsI at 19:58
#found at 
#https://gist.github.com/gyu-don/3777bfa02d2e86cfa9fb64084f3c42dc 

def fizzbuzz(i):
    i-=1
    return i%3//2*"Fizz"+i%5//4*"Buzz"or-~i

for n in range(1,31):
    print(fizzbuzz(n))

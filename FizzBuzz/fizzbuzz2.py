#fizz buzz as seen on
#https://www.youtube.com/watch?v=FyCYva9DhsI at 19:43

def fizzbuzz(n):
    result = ''
    if n%3 == 0:
        result +='fizz'
    if  n%5 == 0:
        result +='buzz'
    if not result:
        result = n
    return result

for n in range(1,31):
    print(fizzbuzz(n))

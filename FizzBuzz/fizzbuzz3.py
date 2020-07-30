#fizz buzz inspired by 
#https://www.youtube.com/watch?v=FyCYva9DhsI at 19:58
#found at 
#https://code.sololearn.com/cn6fJ65with0/#py 

def fizzbuzz(x):
    return "Fizz"[x%3*4:]+"Buzz"[x%5*4:] or x

for n in range(1,31):
    print(fizzbuzz(n))

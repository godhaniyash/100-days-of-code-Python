def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def fibo(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    return fibo(a-1) + fibo(a-2)
print(fibo(10))
















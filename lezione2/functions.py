def factorial(copa):
    x=1
    for i in range(2,copa+1):
        x=i*x
    return x

def fib(ferra):
    if ferra==1 or ferra==2:
        return 1
    return fib(ferra-1)+fib(ferra-2)


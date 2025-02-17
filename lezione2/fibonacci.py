#sequenza di Fibonacci

from functions import fib

n = int(input("inserisci un numero: "))

numbers = []

for i in range (1,n+1):
    numbers.append(fib(i))

print("i primi", n, "numeri della successione di Fibonacci sono", numbers)
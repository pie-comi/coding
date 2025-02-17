import lezione1.numeri_primi as numeri_primi

from lezione1.numeri_primi import is_prime

N = int(input('Inserisci un numero intero: '))

numeri_primi = []

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range (2, N+1):
   if is_prime(i):          # is_prime è già True di default, quindi non serve scrivere if is_prime==True:, basta scrivere if is_prime:.
        numeri_primi.append(i)

print (f'I numeri primi da 1 a {N} sono:', (numeri_primi))
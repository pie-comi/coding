from functions import is_prime

N = int(input('Inserisci un numero intero: '))

numeri_primi = []


for i in range (2, N+1):
   if is_prime(i):          
        numeri_primi.append(i)

print (f'I numeri primi da 1 a {N} sono:', (numeri_primi))
N = int(input('Inserisci un numero intero: '))

numeri_primi = []

for i in range (2, N+1):
    is_prime = True
    for l in range (2, i):
        if i%l==0:
            is_prime = False
    if is_prime:
        numeri_primi.append(i)

print (f'I numeri primi da 1 a {N} sono:', (numeri_primi))

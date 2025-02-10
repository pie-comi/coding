#l = [1,2,3,4,5]
#print(l[3])

#d={'a':1, 'b':2, 'c':3}
#print (d['a'])

N = int(input("inserisci un numero: "))

tot = 0

for i in range(1, N+1):
    tot = tot + i
# i=1

# while i <= N:
#      tot = i + tot
#      i = i + 1

print (f'la somma dei numeri fino a {N} è',tot)
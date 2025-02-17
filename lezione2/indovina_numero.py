print ("Ho scelto un numero tra 1 e 100. Prova a indovinarlo!")

import random 

n = random.randint(0,100)

tries=0

is_winner=False

while is_winner==False:
    x = int(input("Inserisci il tuo numero: "))
    if x < n:
        is_winner=False
        print("Troppo basso! Prova ancora")
        tries=tries+1
    if x > n:
        is_winner=False
        print("Troppo alto! Prova ancora")
        tries=tries+1
    if x==n:
        is_winner = True
        print ("Bravo shugar! Hai indovinato")


lucky=10-tries
print (f"Hai {lucky} possibilità su 10 con la ceci")




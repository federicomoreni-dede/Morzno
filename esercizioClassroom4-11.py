#esercizio classroom 4 11
età=int(input("inserisci la tua età:"))
nome=input("inserisci il tuo nome:")
if età%3==0 and(età%2!=0):
    print (nome[0:2]+nome[-2:])
else:
    print (nome[2:-2])
    

#stringa esercizio
stringa=input("inserisci un nome, delle lettere:")
l=len(stringa)
if l>=3:
    print(stringa[1:-1])
else:
    print("il numero dei caratteri deve essere uguale o maggiore di 3")
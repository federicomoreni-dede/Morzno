#esercizio 9 selezione
nome=input("inserisci un nome:")
nome2=input("inserisci un nome:")
l=(len(nome)//2)
l1=(len(nome2)//2)
parola=nome[:l]+nome2[l1:]
print(parola)

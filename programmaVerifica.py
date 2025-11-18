#programma verifica
nome=input("inserisci un nome:")
cognome=input("inserisci un cognome:")
pr=int(input("inserisci la posizione sul registro:"))
if pr<=0:
    print("immettere valori positivi")
else:
    if pr%2==0 or pr%5==0:
        x=nome[:-1]+cognome[1:]
    else:
        l=len(nome)
        l1=len(cognome)
        if l>4 and l1>=5:
            x=nome[-3:]+cognome[0:4]
        else:
            x=cognome+nome
print(x)
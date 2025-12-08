#esPalindromo
parola=str(input("inserisci una parola:"))
l=len(parola)
l1=l//2
conta=0
while conta<=l1:
    if l%2!=0:
        if parola[0]==parola[-1]:
            parola=parola[1:-1]
            conta+=1
            risultato="parola palindroma"
        else:
            conta+=1
            risultato="parola NON palindroma"
    else:
        while conta<l1-1:
            if parola[0]==parola[-1]:
                parola=parola[1:-1]
                conta+=1
                risultato="parola palindroma"
            else:
                conta+=1
                risultato="parola NON palindroma"
        if parola[0]==parola[-1+1]:
            risulato="parola palindroma"
            conta+=1
        else:
            risultato="parola NON palindroma"
            conta+=1    
print(risultato)
    
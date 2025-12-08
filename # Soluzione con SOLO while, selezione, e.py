parola = str(input("inserisci una parola: "))
errore = 0
while len(parola) > 1 and errore == 0:
    if parola[0] != parola[-1]:     
        errore = 1
    else:
        parola = parola[1:-1]
if errore == 0:   
    risultato = "parola palindroma"
else:
    risultato = "parola NON palindroma"
print(risultato)
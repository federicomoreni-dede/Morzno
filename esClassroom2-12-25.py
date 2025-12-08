#esercizio_coding_2/12/25
stop=int(input("inserisci un numero di stop"))
n=int(input("inserisci un numero:"))
if stop<=0:
    print("non può inserire valori negativi")
else:
    conta=1
    massimo=n
    while conta<stop:             
        n=int(input("inserisci un numero:"))
        conta+=1
        if n>massimo:
            massimo=n
print(massimo)
parola=input("e")
print(parola[1:-1])


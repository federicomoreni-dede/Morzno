#esercizio 21
media=0
conta=0
stop=int(input("inserisci numero di stop"))
while conta <stop:
    nome=input("inserisci un nome:")
    voto=int(input("inserisci un voto da 18 a 30:"))
    conta+=1
    if voto<18 or voto>30:
        print("i voti vanno dal 18 al 30, riprova")
    else:
        media=media+voto
media1=media/conta
print(media1)


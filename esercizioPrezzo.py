qP=int(input("inserisci la quantità del prodotto:"))
PP=float(input("inserisci il prezzo al pezzo, prodotto:"))
PI=qP*PP
PS=PI-((1/3)*PI)
if qP<3:
    print(PI)
else:
    print(PS)


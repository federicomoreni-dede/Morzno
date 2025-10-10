voti_primo=int(input("inserisci i voti del primo candidato:"))
voti_secondo=int(input("inserisci i voti del secondo candidato:"))
totale_voti=(voti_primo+voti_secondo)
if totale_voti==0:
    print("Non sono stati inseriti voti validi.")
#continua solo se ci sono voti
else:
    #Calcolo percentuali
    percentuale_primo_su_100=(100*voti_primo)/totale_voti
    percentuale_secondo_su_100=(100*voti_secondo)/totale_voti
    #ballottaggio
    if percentuale_primo_su_100==percentuale_secondo_su_100:
        print("i voti sono in parità, nessun candidato ha vinto")
    else:
        if percentuale_primo_su_100>percentuale_secondo_su_100:
            print("il primo candidato ha vinto")
    #se non si sono verificate le altre due
        else:
            print("il secondo candidato ha vinto") 
print("percentuale_primo=",percentuale_primo_su_100)
print("percentuale_secondo=",percentuale_secondo_su_100)
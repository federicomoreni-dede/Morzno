#esercizi selezione 17 ottobre
import math
import os
def esercizio_1():
    #scrivi un programma che legge tre numeri interi e li stampa in ordine decrescente
    n1=int(input("inserisci un numero:"))
    n2=int(input("inserisci un numero:"))
    n3=int(input("inserisci un numero:"))
    if n1>n2>n3:
        print(n1,n2,n3)
    elif n2>n3>n1:
        print(n2,n3,n1)
    elif n3>n1>n2:
        print(n3,n1,n2)
    elif n1>n3>n2:
        print(n1,n3,n2)
    elif n3>n2>n1:
        print(n3,n2,n1)
    else:
        print(n2,n1,n3)
    return
def esercizio_2():
    #Scrivere un programma che legge un voto e dice se insufficiente grave, leggero o sufficiente
    voto=float(input("inserisci un voto scolastico (0-10):"))
    if voto<=4:
        print("insufficienza grave,studia!!!")
    elif 4<voto<6:
        print("insufficienza leggera,recupera!")
    elif voto>=6:
        print("sufficienza,bravo!")
    return
def esercizio_3():
    #Scrivere un programma che ti dice se il triangolo è rettangolo o meno
    lato1=float(input("inserisci il valore di un lato:"))
    lato2=float(input("inserisci il valore dil un lato:"))
    lato3=float(input("inserisci il valore di un lato:"))
    if (lato1**2+lato2**2)==lato3**2:
        print ("triangolo rettangolo")
    elif (lato2**2+lato3**2)==lato1**2:
        print ("triangolo rettangolo")
    elif (lato1**2+lato3**2)==lato2**2:
        print ("triangolo rettangolo")
    else:
        print("triangolo NON rettangolo")
    return
def esercizio_5():
    #Scrivere un programma che converte la temperatura Celsius in Kelvin e Fahreineit
    tempC=float(input("inserisci una tmperatura in gradi Celsius: "))
    tempK=tempC+273.15
    tempF=(9/5*tempC)+32
    if tempC>-273.15:
        print("temperatura in Kelvin:",tempK,"K")
        print("temperatura in Fahreneit",tempF,"F")
    else:
        print("valore della variabile non corretto")
    return
def esercizio_6():
    #Scrivere un programma che stampa di una stringa lunga almeno 3 caratteri, tutto tranne il primo e l'ultimo carattere
    stringa=input("inserisci un nome, delle lettere:")
    l=len(stringa)
    if l>=3:
        print(stringa[1:-1])
    else:
        print("il numero dei caratteri deve essere uguale o maggiore di 3")
    return
def esercizio_7():
    #Scrivere un programma che sostituisce in una stringa il primo carattere con la lettera sucessiva nell'alfabeto
    parola=input("inserisci una parola: ")
    nuova_lettera = chr(ord(parola[0])+1)
    nuova_parola = nuova_lettera + parola[1:]
    print(nuova_parola)
    return
def esercizio_8():
    parola=input("inserisci una parola:")
    if parola[0]==parola[-1]:
        print("prima e l'ultima lettera uguali")
    else:
        print("prima e ultima lettera diverse")
    return
def esercizio_9():
    #Scrivere un programma che compone due stringhe per eccesso, una con l'inizio parola, l'altra con la fine
    nome=input("inserisci un nome:")
    nome2=input("inserisci un nome:")
    l=(len(nome)//2)
    l1=(len(nome2)//2)
    parola=nome[:l]+nome2[l1:]
    print(parola)
    return
def esercizio_10():
    #Scrivere un programma che compone tre stringhe inserite da tastiera
    s2=input("inserisci una parola:")
    s1=input("inserisci una parola:")
    l1=len(s1)
    l2=len(s2)
    n1=int(input("inserisci un numero naturale:"))
    n2=int(input("inserisci un numero naturale:"))
    parola=s1[:n1]+s2[n1:n2+1]+s1[n2+1:]
    parola1=s2[:n2]+s1[n2:n1+1]+s2[n1+1:]
    if n1 and n2<l1 and l2:
        if n1>n2:
            print(parola1)
        else:
            print(parola)    
    else:
        print("variabile non corretta")
def principale():
    try:
        esercizio_1,esercizio_2,esercizio_3,esercizio_5,esercizio_6,esercizio_7,esercizio_8,esercizio_9,esercizio_10
    except Exception as e:
        os.system("cls")
        os.system("colour 4")
        print("si è verificato un errore:'{e}")
    finally:
        os.system("pause")
        os.system("colour 7")
        os.system("cls")
    return
principale






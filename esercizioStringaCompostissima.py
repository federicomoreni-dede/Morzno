#esercizio stringa compostissima
s1=input("inserisci una parola:")
s2=input("inserisci una parola:")
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
    
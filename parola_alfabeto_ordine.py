#parola alfabeto ordine
parola=input("inserisci una parola: ")
nuova_lettera = chr(ord(parola[0])+1)
nuova_parola = nuova_lettera + parola[1:]
print(nuova_parola)
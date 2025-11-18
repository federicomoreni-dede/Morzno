#riprova verifica
x=int(input("inserisci un numero intero:"))
if x<=19:
    x=25-x
if x%2==0:
    x=x*x-32
else:
    if(x>13):
        x=2*x-25
    else:
        x=x-2
print(x)

s = str(input("inserisci la stringa in cui cercare: "))
s1 = str(input("inserisci la stringa da cercare: "))
l = len(s)
l1 = len(s1)
if l1 > l:
    print("nope")    
pos= 0
risultato = False
while pos <= l - l1:
    pos1= 0    
    while pos1 < l1 and s[pos + pos1] == s1[pos1]:
        pos1+= 1    
    if pos1== l1:
        risultato = True
        break    
    pos+= 1
if risultato:
    print("yess")
else:
    print("nope")
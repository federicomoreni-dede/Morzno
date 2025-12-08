#esercizioSottostringa
s=str(input("inserisci la stringa in cui cercare:"))
s1=str(input("inserisci la stringa da cercare:"))
pos=0
l=len(s)
l1=len(s1)
i1=s1[0]#iniziale della stringa da cercare
if l<=l1:
    print("non possibile")
else:
    while pos<=l-l1:
        if s[pos:pos+l1]==s1[0:]:#SUCCESS
            r = "sì"
            break
        else:
            r="no"
            pos+=1
    print(r)

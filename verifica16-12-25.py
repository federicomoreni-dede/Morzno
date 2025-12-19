#verifica16-12-25
s=str(input("ins stringa:"))
l=len(s)
if l<=0:
    print("non possibile")
    exit()
pos=0
s1=""
while pos<=l-1:
    while s[pos]=="a"or s[pos]=="e" or s[pos]=="i" or s[pos]=="o" or s[pos]=="u":
        s1=s1+s[pos]
        pos+=1
    s1=s1+s[pos]+"o"+s[pos]
    pos+=1
print(s1)
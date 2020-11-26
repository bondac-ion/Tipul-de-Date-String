s=str(input("introduceti sirul de date:"))
nr=0
nc=0
nmin=0
for i in s:
    if ((ord(i))>=65) and ((ord(i))<=90):
        nr+=1

print ("Numarul de majuscule este",nr)
for i in s:
    if (ord(i)>=48) and (ord(i)<=57):
        nc+=1

print("Numarul de cifre este:",nc)
for i in s:
    if (ord(i)>=97) and (ord(i)<=122):
        nmin+=1

print("Numarul de minuscule este:",nmin)

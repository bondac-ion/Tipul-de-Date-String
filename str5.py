"""Se citeste un sir de caractere care reprezinta CNP-ul unei persoane. Să se verifice corectitudinea lui:numărul de caractere să fie 13 și toate caracterele să fie cifre."""
a=str(input("dati un idnp:"))
n=0
if len(a)!=13:
    print("nu este cnp")
else:
    for i in a:
        if ord(i)>=48 and ord(i)<=57:
            n+=1

if len(a)==13 and n==13:
    print("poate fi cnp")
else:
    print("nu este cnp")


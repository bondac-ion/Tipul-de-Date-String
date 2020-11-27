a=str(input("dati un cuvint:"))
b=str(input("dati un cuvint:"))
c=str(input("dati un cuvint:"))
d=str(input("dati un cuvint:"))
e=""
if (len(a) > 2) or (len(b) > 2) or (len(c) > 2) or (len(d) > 2):
    e=a[0:2]+b[0]+c[:3]+d[:(len(d)//2)]
else:
    print("un civant are mai putin de 3 cifre")

print(a)
print(b)
print(c)
print(d)
print(e)
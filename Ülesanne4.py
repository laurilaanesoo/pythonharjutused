# Ülesanne 4
# Lauri Laanesoo
# 03.02.2022

#Müük

hind= input("Sisesta toote hind: ")
if hind > 10:



#Juubel
aasta = input("Sisesta sünniaeg kujul dd.mm.yyyy: ")
a,b,c = aasta.split(".")
aasta = 2022 - int(c)
if aasta%5==0:
    print("Sul on juubel")
else:
    print("Sul ei ole juubel")


#Matemaatika
a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))
c = input("Millist tehet tahad teha? (+ - * /")
if c=="+":
    d= a + b
elif c=="-":
    d= a - b
elif c=="*":
    d= a * b
else:
    d= a / b
print(f"{a}{c}{b}={d}")


#Ruut
a = int(input("Sisesta ruudu esimene külg: "))
b = int(input("Sisesta ruudu teine külg: "))

if a==b:
    print("Kujund on ruut")
else:
    print("Kujund ei ole ruut")

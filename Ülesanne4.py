# Ülesanne 4
# Lauri Laanesoo
# 03.02.2022

#Ruutude ja kuupide tabel

print(f" {'Arv':4} {'Ruut':6} {'Kuup':10}")
for h in range(1,11):
    print(f"{h:5} {h**2:5} {h**3:5} ")



#Pank
konto = 0
raha = 10000 #int(input("Sisesta raha summa, mis tahad panka panna: "))
intress = 0.05
aastad = 5 # int(input("Vali aastad: "))
konto += raha # Lisab kontole raha
print(f" {'Aasta':4} {'Algsumma':10} {'Intress':10} {'Aasta lõpuks':10}")
for i in range(aastad):
    kasum = konto*intress
    print(f"{i:4} {konto:10.2f} {kasum:10.2f} {konto+kasum:10.2f}")
    konto+=kasum

#Arvamismäng
import random

loop = 1
korrad = 1
suv = random.randint(1,10)

while loop==1:
    
    if korrad <= 3:
        arv = int(input("Arva ära arv 1-10: "))
    else:
        veel = input("Kas soovid veel mängida? jah/ei: ")
        
        if veel =="jah":
            korrad = 0
        else:
            loop = 0
    korrad +=1
    
    if arv==suv:
        print("Arvasid arvu ära")
        loop = 0
    else:
        print("Arva uuesti")
    
    print(suv, arv, korrad)

print("Mäng läbi")


#Viisikud
for g in range(1,100):
    if g%5==0:
        print(g)
    else:
        print("")


#Korrutustabel
for k in range(1,11):
    arv = 5
    print(f"{arv} x {k} = {k*arv}")


#Paaris paaritu
for i in range(1,101):
    if i%2==0:
        print(i,"paaris")
    else:
        print(i,"paaritu")
        

#Loto
import random
arv = random.randint(10000,99999)
print(arv)


#Tärnid
for i in range(1,6):
    for j in range(1,6):
        print("* ",end="")
    print()

for i in range(1,6):
    print("* "*i)

k=5
for i in range(1,6):
    print("* "*k)
    k = k - 1

#Jalgpalli meeskond
sugu = input("Sisesta oma sugu: ")
if sugu == "m":
    vanus = int(input("Sisesta oma vanus: "))
    if vanus >= 16 and vanus <= 18:
         print("Said jalgpalli meeskonda")
    else:
         print("Ei saanud jalgpalli meeskonda")
else:
    print("Ei saanud jalgpalli meeskonda")



#Müük
hind= int(input("Sisesta toote hind: "))
if hind > 10:
    allahindlus = hind * 0.2
else:
    allahindlus = hind * 0.1
print(hind-allahindlus)


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
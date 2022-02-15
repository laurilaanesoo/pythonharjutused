#Ülesanne7

import math

def kuup(a):
    v = a ** 3
    return v 

def kera(r):
    v = round(4/3*math.pi*r**3,2)
    return v

def koonus(r,h):
    v = round(1/3*math.pi*r**2*h,2)
    return v
def silinder(r,h):
    v = round(math.pi*r**2*h,2)
    return v

loop = 1

print("Ruumala leidmine")
print("Vali kujund:\n1. Kuup\n2. Kera \n3. Koonus\n4. Silinder\n5. VÄLJU")
valik=int(input("Vali kujundi number: "))

if valik == 1:
    print("Valisid kuubi")
    a = valik=int(input("Sisesta kuubi külje pikkus: "))
    print(kuup(a))

elif valik ==2:
    print("Valisid kera")
    b = valik=int(input("Sisesta kera raadius: "))
    print(kera(b))
    
elif valik ==3:
    print("Valisid koonuse")
    r = valik=int(input("Sisesta koonuse raadius: "))
    h = valik=int(input("Sisesta koonuse kõrgus: "))
    print(koonus(r,h))

elif valik ==4:
    print("Valisid silindri")
    r = valik=int(input("Sisesta silindri raadius: "))
    h = valik=int(input("Sisesta silindri kõrgus: "))
    print(silinder(r,h))

elif valik ==5:
   loop = 0
   
   
#Teeb funktsiooni "nimi"
def tervita(nimi, keel="de"):
    if keel=="et":
        print (f"Tere, {nimi}!")
    elif keel=="en":
        print(f"Hi {nimi}!")
    else:
        print(f"Hallo {nimi}!")

nimi = input("Sisesta oma nimi: ")
keel = input("Vali keel et/en/de: ")
#Funktsiooni käivitamine
tervita(nimi,keel)
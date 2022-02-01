import math
# Harjutus 2
# Lauri Laanesoo
# 31.01.2022


#Kütusekulu
l = int(input("Sisesta tangitud liitrid: "))
km = int(input("Sisesta läbitud kilomeetrid: "))
liitrid = l/(km/100)
print(liitrid)
        

#Arvusüsteemid
a = int(input("Sisesta täisarv: "))
print(bin(a))
print(oct(a))

#Ajateisendus
minutid = int(input("Sisesta aeg minutites: "))
tunnid = minutid//60
minut = minutid%60
print(minutid, "minutit on",tunnid,":",minut)


#Kolmnurga hüpotenuus
a = 16
b = 9
hupotenuus = 16^2 + 9^2
c = math.sqrt(a^2+b^2)
print("Kolmnurga hüpotenuus on",c, "cm")


#Rulluisutajad
kiirus = 29.9
aeg = 24
pikkus = 29.9/24
print("Rulluisutaja jõuab",pikkus, "km")


#Pitsa
pitsa = 12.9
sobrad = 3
jootraha = 0.1
maksma = 12.90*3*0.1
print("Igaüks peab maksma",maksma, "€")


#Toote hind
hind = 36.75
soodus = 0.4
kogus = 3
summa = 36.75*0.4*3
print("Kolme toote summa on:",summa,"€")


#Kolmnurga ümbermõõt
a,b,c = 3,4,5
p=a+b+c
print("Kolmnurga ümbermõõt on:",p,"cm")